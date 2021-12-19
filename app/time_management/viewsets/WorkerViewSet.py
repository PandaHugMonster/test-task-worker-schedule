from rest_framework import viewsets
from .. import models
from .. import serializers


class WorkerViewSet(viewsets.ModelViewSet):
	queryset = models.Worker.objects.all()
	serializer_class = serializers.WorkerSerializer
