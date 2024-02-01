from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Educacion, Experiencia, AcercaDe, Proyectos
from .serializers import EducacionSerializer, ExperienciaSerializer, ProyectosSerializer, AcercaDeSerializer


class BaseModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_permissions(self):
        # Permitir GET sin autenticación, requerir autenticación para otras operaciones
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        else:
            return super().get_permissions()


class EducacionViewSet(BaseModelViewSet):
    queryset = Educacion.objects.all().order_by('-creado_en')  # Ordenar por fecha de creación descendente
    serializer_class = EducacionSerializer


class ExperienciaViewSet(BaseModelViewSet):
    queryset = Experiencia.objects.all().order_by('-creado_en')
    serializer_class = ExperienciaSerializer


class ProyectosViewSet(BaseModelViewSet):
    queryset = Proyectos.objects.all().order_by('-creado_en')
    serializer_class = ProyectosSerializer


class AcercaDeViewSet(BaseModelViewSet):
    queryset = AcercaDe.objects.all()
    serializer_class = AcercaDeSerializer