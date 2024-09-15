from rest_framework import serializers
from ..models.extras import Extras


class ExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extras
        fields = '__all__'
