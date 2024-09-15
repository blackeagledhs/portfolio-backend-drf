from blackeagle.models import Badge
from blackeagle.serializers import BadgeSerializer
from blackeagle.views import BaseModelViewSet


class BadgeViewSet(BaseModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
