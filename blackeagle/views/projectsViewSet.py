from blackeagle.models import Projects
from blackeagle.serializers import ProjectsSerializer
from blackeagle.views import BaseModelViewSet


class ProjectsViewSet(BaseModelViewSet):
    queryset = Projects.objects.all().order_by('-created_on')
    serializer_class = ProjectsSerializer
