from django.shortcuts import render
from rest_framework import viewsets
from .models import CameraManagement
from .serializers import CameraManagementSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class CameramanageViews(viewsets.GenericViewSet):
    queryset = CameraManagement.objects.all()
    serializer_class = CameraManagementSerializer
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            camera = serializer.save()
            return Response({"message": "Camera Setup Successfully!", "cam_id": camera.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
            