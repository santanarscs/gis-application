from rest_framework import viewsets, response
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Tool, ToolInput
from .serializers import ToolInputSerializer, ToolsSerializer
class ToolViewSet(viewsets.ModelViewSet):
  '''
    Contem informação sobre command line
  '''
  queryset = Tool.objects.all()
  lookup_field = 'id'
  serializer_class = ToolsSerializer

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    self.get_serializer().destroy(instance)
    print('Instance destroyed!')
    return response.Response(status=HTTP_204_NO_CONTENT)
