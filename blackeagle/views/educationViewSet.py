from blackeagle.models import Education
from blackeagle.serializers import EducationSerializer
from blackeagle.views import BaseModelViewSet


class EducationViewSet(BaseModelViewSet):
    queryset = Education.objects.all().order_by('-year')
    serializer_class = EducationSerializer
