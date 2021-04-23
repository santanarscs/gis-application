from rest_framework_mongoengine import serializers
from .models import Infrastructure


class InfrastructureSerializer(serializers.DocumentSerializer):
  class Meta:
    model = Infrastructure
    fields = '__all__'