from rest_framework import viewsets, permissions
from .models import Educacion, Experiencia, AcercaDe, Proyectos
from .serializers import EducacionSerializer, ExperienciaSerializer, ProyectosSerializer, AcercaDeSerializer


class EducacionViewSet(viewsets.ModelViewSet):
    queryset = Educacion.objects.all().order_by('-creado_en')  # Ordenar por fecha de creación descendente
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EducacionSerializer


class ExperienciaViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all().order_by('-creado_en')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ExperienciaSerializer


class ProyectosViewSet(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all().order_by('-creado_en')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProyectosSerializer


class AcercaDeViewSet(viewsets.ModelViewSet):
    queryset = AcercaDe.objects.all().order_by('-creado_en')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AcercaDeSerializer