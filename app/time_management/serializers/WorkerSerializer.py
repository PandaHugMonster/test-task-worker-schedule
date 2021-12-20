from rest_framework import serializers

from .. import models


class WorkerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Worker
		fields = ['id', 'name', 'birthdate', 'max_shifts_per_week']
		extra_kwargs = {
			'id': {'read_only': True},
			'max_shifts_per_week': {'default': 4},
		}
