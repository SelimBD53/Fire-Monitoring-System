from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('user-registration', views.UsercreateView, basename='user_registration')
urlpatterns = [
    path('', views.index, name='home'),
    path('', include(router.urls)),
]