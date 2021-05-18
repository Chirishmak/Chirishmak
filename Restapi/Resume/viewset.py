from rest_framework import viewsets
from . import models
from . import serializers

class resumeViewSet(viewsets.ModelViewSet):
    queryset=models.resume.objects.all()
    serializer_class = serializers.resumeSerializer