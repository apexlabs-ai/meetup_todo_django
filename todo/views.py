from rest_framework import viewsets, permissions

from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    pagination_class = None
    permission_classes = (permissions.AllowAny, )
    queryset = Todo.objects.all()
