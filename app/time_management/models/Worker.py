from django.db import models


class Worker(models.Model):
	"""
		Represents Worker

		name - Full worker name
		birthdate - Birthdate of the worker for better identification
		max_shifts_per_week - Max amount of shifts per 1 week for this worker. Applicable only when
			settings.TIME_MANAGEMENT_APP['LIMIT_WEEKLY_SHIFTS'] is True and max_shifts_per_week is not empty.
	"""

	name = models.CharField(max_length=255)
	birthdate = models.DateField(null=True)
	max_shifts_per_week = models.IntegerField(null=True, default=4)

	def __str__(self):
		return f"[ {self.birthdate} ] {self.name}"
