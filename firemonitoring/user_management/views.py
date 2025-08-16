from django.shortcuts import render
from .models import UserProfile
from .serializers import UserProfileSerializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'home.html')

class UsercreateView(viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    
    def create(self, request):
        serializer =self.get_serializer(data=request.data)
        if serializer.is_valid():
            user_acc = serializer.save()
            return Response({"message": "User Profile Created Successfully", 'user_id': user_acc.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)