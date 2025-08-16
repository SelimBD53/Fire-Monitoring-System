from rest_framework import serializers
from .models import CameraManagement

class CameraManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraManagement
        fields = "__all__"

    def create(self, validated_data):
        cameraprofile = CameraManagement.objects.create(**validated_data)
        cameraprofile.save()
        return cameraprofile    
    