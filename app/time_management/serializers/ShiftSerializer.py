import datetime

from rest_framework import serializers
from .. import models


class ShiftSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Shift
		fields = ['target_dt', 'worker', 'memo', 'cached_worker_name', ]
		extra_kwargs = {
			'cached_worker_name': {'read_only': True},
		}

	def validate_worker(self, val: models.Worker):
		try:
			dt = datetime.datetime.fromisoformat(self.initial_data['target_dt'])
		except ValueError:
			return val

		if not val:
			raise serializers.ValidationError(f"Worker field is required")

		today_shift: models.Shift = val.shifts.filter(target_dt__date=dt.date()).first()

		if today_shift:
			raise serializers.ValidationError(f"Worker already having a shift this day: {today_shift.target_dt}")

		# TODO  Implement better validation with strict shifts and with non-strict ones
		# TODO  Improve validation and empty/optional/required fields
		return val
