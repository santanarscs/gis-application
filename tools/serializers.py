from rest_framework_mongoengine import serializers
from .models import ToolInput, Tool


class ToolsSerializer(serializers.DocumentSerializer):
  class Meta:
    model = Tool
    fields = '__all__'