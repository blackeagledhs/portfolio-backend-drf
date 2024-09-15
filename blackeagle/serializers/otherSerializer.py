from rest_framework import serializers
from ..models.other import Other


class OtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Other
        fields = '__all__'
