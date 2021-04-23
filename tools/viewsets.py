from rest_framework_mongoengine import viewsets
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Tool
from .serializers import  ToolsSerializer



class ToolViewSet(viewsets.ModelViewSet):
  '''
    Contem informação sobre ferramentas
  '''
  lookup_field = 'id'
  serializer_class = ToolsSerializer

  def get_queryset(self):
      return Tool.objects.all()
