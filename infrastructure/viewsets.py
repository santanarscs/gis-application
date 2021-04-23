from rest_framework_mongoengine import viewsets
from .models import Infrastructure
from .serializers import  InfrastructureSerializer




class InfrastructureViewSet(viewsets.ModelViewSet):
  '''
    Contem informação sobre Infraestrutura
  '''
  lookup_field = 'id'
  serializer_class = InfrastructureSerializer

  def get_queryset(self):
      return Infrastructure.objects.all()
