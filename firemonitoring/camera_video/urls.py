from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('camera-setup', views.CameramanageViews, basename='camera_setup_view')
urlpatterns = [
    path('', include(router.urls)),
]