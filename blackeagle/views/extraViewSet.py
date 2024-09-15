from blackeagle.models import Extras
from blackeagle.serializers import ExtrasSerializer
from blackeagle.views import BaseModelViewSet


class ExtraViewSet(BaseModelViewSet):
    queryset = Extras.objects.all()
    serializer_class = ExtrasSerializer