import datetime

from django.db import models
from .Worker import Worker


class Shift(models.Model):
	"""
		Shift represents a single record about a shift per Worker (but not limited to a Worker)

		cached_worker_name - is needed in case of deletion of worker's record, to preserve the information
		about history of shifts.
	"""

	worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, related_name='shifts')

	cached_worker_name = models.CharField(max_length=255, null=True)
	target_dt = models.DateTimeField()
	updated_dt = models.DateTimeField(null=True)
	memo = models.CharField(max_length=1024, null=True)

	def save(self, *args, **kwargs):
		self.cached_worker_name = self.worker.name
		self.updated_dt = datetime.datetime.now()
		super(Shift, self).save(*args, **kwargs)
