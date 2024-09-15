from blackeagle.models import About
from blackeagle.serializers import AboutSerializer
from blackeagle.views import BaseModelViewSet


class AboutViewSet(BaseModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

