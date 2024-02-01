from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EducacionViewSet, ExperienciaViewSet, ProyectosViewSet, AcercaDeViewSet

router = DefaultRouter()
router.register(r'educacion', EducacionViewSet)
router.register(r'experiencia', ExperienciaViewSet)
router.register(r'proyectos', ProyectosViewSet)
router.register(r'acerca-de', AcercaDeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]