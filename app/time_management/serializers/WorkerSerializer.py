from rest_framework import serializers
from .. import models


class WorkerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Worker
		fields = ['name', 'birthdate', 'max_shifts_per_week']
