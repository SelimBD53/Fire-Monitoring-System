from django.db import models
from user_management.models import UserProfile, Company
# Create your models here.
choise = {
    ("Panding", "Panding"),
    ("Successfull", "Successfull")
}
class CameraManagement(models.Model):
    name = models.CharField(max_length=128, null=True)
    location = models.CharField(max_length=128)
    ip_address = models.CharField(max_length=125)
    status = models.CharField(max_length=123, choices=choise)
    created_at = models.DateTimeField(auto_now_add=True)
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="cameras")
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="cameras")
    
    def __str__(self):
        return self.ip_address
    