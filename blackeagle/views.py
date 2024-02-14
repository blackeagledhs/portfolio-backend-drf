from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Education, Experience, About, Projects
from .serializers import EducationSerializer, ExperienceSerializer, ProjectsSerializer, AboutSerializer


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

        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        else:
            return super().get_permissions()


class EducationViewSet(BaseModelViewSet):
    queryset = Education.objects.all().order_by('-created_on')
    serializer_class = EducationSerializer


class ExperienceViewSet(BaseModelViewSet):
    queryset = Experience.objects.all().order_by('-created_on')
    serializer_class = ExperienceSerializer


class ProjectsViewSet(BaseModelViewSet):
    queryset = Projects.objects.all().order_by('-created_on')
    serializer_class = ProjectsSerializer


class AboutViewSet(BaseModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
