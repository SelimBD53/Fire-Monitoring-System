from argparse import Action
from django.shortcuts import render
from .models import UserProfile
from .serializers import UserProfileSerializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

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
    
    @action(detail=False, methods=['post'], url_path='verify-otp')
    def Verify_otp(self, request):
        otp_phone = request.data.get('phone')
        otp_code = request.data.get('otp')
        
        if not otp_phone or not otp_code:
            return Response({"message": "Phone Number and OTP is Required!"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user_account = UserProfile.objects.get(phone=otp_phone)
            
            if user_account.otp == otp_code:
                user_account.user.is_active = True
                user_account.user.save()
                
                user_account.otp = None
                user_account.save()
                return Response({"message": "OTP Verification Successfully. User is Now Active!"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid OTP!"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"An error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)     
       
            