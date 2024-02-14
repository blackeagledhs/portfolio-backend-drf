from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EducationViewSet, ExperienceViewSet, ProjectsViewSet, AboutViewSet

router = DefaultRouter()
router.register(r'education', EducationViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'projects', ProjectsViewSet)
router.register(r'about', AboutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
