from core.Neurodivergente import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'profile', views.ProfileViewSet)