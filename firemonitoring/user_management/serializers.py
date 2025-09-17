from rest_framework import serializers
from .models import UserProfile, Company
from django.contrib.auth.models import User
import random
from .sms_otp import send_sms
class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'address', 'phone']
        extra_kwargs = {
            'id': {'required': False} 
        }
        
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'username': {'read_only': True}
        }
    
class UserProfileSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    company = CompanySerializers()
    class Meta:
        model = UserProfile
        fields = "__all__"
    
    def validate(self, data):
        if 'user' in data:
            user_data = data['user']
            if 'email' in user_data:
                email = user_data['email']
                if User.objects.filter(email=email).exists():
                    raise serializers.ValidationError({"message": "Email Already Exist!"})
        if 'phone' in data:
            phone = data['phone']
            if len(phone) != 11 or not phone.startswith('01') :
                raise serializers.ValidationError({"message": "Phone Number is incorrect"})
        return data
    
    def create(self, validated_data):
        try:
            otp_code = str(random.randint(100000, 999999))
            user = validated_data.pop('user')
            firstname = user.get('first_name')
            lastname = user.get('last_name')
            phone = validated_data.get('phone')
            user['username'] = f"{firstname}_{lastname}_{phone[-2:]}"
            user_instance = User.objects.create(**user)
            
            company_data = validated_data.pop('company', None)

            if not company_data:
                raise serializers.ValidationError({"message": "Company data is required!"})
            
            if 'id' in company_data: 
                company_instance = Company.objects.get(id=company_data['id'])

            else:
                company_instance = Company.objects.create(**company_data)

            user_profile = UserProfile.objects.create(user=user_instance, company=company_instance, otp=otp_code, **validated_data)
            user_profile.save()
            message = f"Dear {firstname} Registration verification OTP is {otp_code}"
            send_sms(phone, message)
            return user_profile
        
        except Exception as e:
            print(e)
            raise serializers.ValidationError({"message : Error from creating User Profile!"})