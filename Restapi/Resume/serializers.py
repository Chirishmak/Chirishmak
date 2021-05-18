from django.db import models
from django.db.models.fields import files
from rest_framework import serializers
from .models import resume

class resumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = resume
        fields = '__all__'

