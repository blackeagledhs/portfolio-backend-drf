from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (EducationViewSet, ExperienceViewSet,
                    ProjectsViewSet, AboutViewSet, BadgeViewSet, OtherViewSet, ExtraViewSet, blank_page, ContactViewSet)

router = DefaultRouter()
router.register(r'education', EducationViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'projects', ProjectsViewSet)
router.register(r'about', AboutViewSet)
router.register(r'badge', BadgeViewSet)
router.register(r'other', OtherViewSet)
router.register(r'extra', ExtraViewSet)
router.register(r'contact', ContactViewSet)


urlpatterns = [
    path('', blank_page, name='blank_page'),
    path('api/', include(router.urls)),
]
