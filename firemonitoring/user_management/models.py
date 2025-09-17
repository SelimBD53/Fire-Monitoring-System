from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
# ROLE = [
#     ("EMP", "Empolyees"),
#     ("AD", "Admin"),
# ]
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # role = models.CharField(max_length=50, choices=ROLE, null=True, blank=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    otp = models.CharField(max_length=10, blank=True, null=True)
    profile_pic = ResizedImageField(size=[300, 300], upload_to='profile_pics', null=True, blank=True, force_format='webp', quality=100)
  
    def __str__(self):
        return self.user.first_name
