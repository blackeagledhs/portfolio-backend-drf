from blackeagle.models import Experience
from blackeagle.serializers import ExperienceSerializer
from blackeagle.views import BaseModelViewSet


class ExperienceViewSet(BaseModelViewSet):
    queryset = Experience.objects.all().order_by('-created_on')
    serializer_class = ExperienceSerializer
