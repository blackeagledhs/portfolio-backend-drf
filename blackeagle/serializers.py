from rest_framework import serializers
from .models import Educacion, Experiencia, Proyectos, AcercaDe

class EducacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educacion
        fields = '__all__'

class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencia
        fields = '__all__'

class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = '__all__'

class AcercaDeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcercaDe
        fields = '__all__'