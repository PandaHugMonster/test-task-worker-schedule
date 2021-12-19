from rest_framework import viewsets
from .. import models
from .. import serializers


class ShiftViewSet(viewsets.ModelViewSet):
	queryset = models.Shift.objects.all()
	serializer_class = serializers.ShiftSerializer
