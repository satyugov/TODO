from rest_framework.viewsets import ModelViewSet

from .models import Project, Tasks
from .serializers import ProjectHyperlinkedModelSerializer, TaskHyperlinkedModelSerializer

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer


class TaskModelViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskHyperlinkedModelSerializer
