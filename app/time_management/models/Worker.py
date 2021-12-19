from django.db import models


class Worker(models.Model):
	name = models.CharField(max_length=255)
	birthdate = models.DateField(null=True)
	max_shifts_per_week = models.IntegerField(null=True)

	def __str__(self):
		return f"[ {self.birthdate} ] {self.name}"
