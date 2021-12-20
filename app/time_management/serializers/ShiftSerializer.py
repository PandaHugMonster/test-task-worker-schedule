import datetime

from django.conf import settings
from rest_framework import serializers
from .. import models


class ShiftSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Shift
		fields = ['id', 'target_dt', 'worker', 'memo', 'cached_worker_name', ]
		extra_kwargs = {
			'id': {'read_only': True},
			'cached_worker_name': {'read_only': True},
		}

	def validate_worker(self, val: models.Worker):
		dt_parsing_format = '%Y-%m-%dT%H:%M'
		try:
			dt = datetime.datetime.strptime(self.initial_data['target_dt'], dt_parsing_format)
		except ValueError:
			raise serializers.ValidationError(f"DateTime value has incorrect format: {self.initial_data['target_dt']}")

		if not val:
			raise serializers.ValidationError(f"Worker field is required")

		limit_weekly_shifts: bool = settings.TIME_MANAGEMENT_APP['LIMIT_WEEKLY_SHIFTS']
		# TODO  Fix non-strict 2-days shift

		if limit_weekly_shifts and val.max_shifts_per_week:
			week_start = dt - datetime.timedelta(days=dt.weekday())
			week_end = week_start + datetime.timedelta(days=6)
			whole_week_shifts = val.shifts.filter(
				target_dt__date__gte=week_start,
				target_dt__date__lte=week_end,
			).count()
			if whole_week_shifts >= val.max_shifts_per_week:
				raise serializers.ValidationError(
					f"Worker has reached limit of shifts per week: {whole_week_shifts}, "
					f"please choose another worker."
				)

		today_shift: models.Shift = val.shifts.filter(target_dt__date=dt.date()).first()

		if today_shift:
			raise serializers.ValidationError(f"Worker already having a shift this day: {today_shift.target_dt}")

		return val

	def validate_target_dt(self, val: datetime.datetime):
		strict_time_slots: bool = settings.TIME_MANAGEMENT_APP['STRICT_TIME_SLOTS']

		if strict_time_slots and (val.hour not in (0, 8, 16) or val.minute != 0):
			raise serializers.ValidationError(
				'Strict timeslot is activated, please use one '
				'of the following values: 00:00, 08:00 or 16:00'
			)

		return val
