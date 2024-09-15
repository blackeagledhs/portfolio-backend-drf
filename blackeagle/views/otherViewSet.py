from blackeagle.models import Other
from blackeagle.serializers import OtherSerializer
from blackeagle.views import BaseModelViewSet


class OtherViewSet(BaseModelViewSet):
    queryset = Other.objects.all()
    serializer_class = OtherSerializer