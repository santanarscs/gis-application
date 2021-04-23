from rest_framework import serializers
from .models import ToolInput, Tool
class ToolInputSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ToolInput
    fields = '__all__'

class ToolsSerializer(serializers.HyperlinkedModelSerializer):
  inputs = ToolInputSerializer(many=True)

  class Meta:
    model = Tool
    fields = ('label', 'description', 'inputs')