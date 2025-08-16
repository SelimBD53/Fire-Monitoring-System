from django.db import models
from user_management.models import UserProfile
# Create your models here.

# class Alert(models.Model):
#     ALERT_TYPE_CHOICES = [
#         ('fire', 'Fire'),
#         ('smoke', 'Smoke'),
#         ('system', 'System'),
#     ]

#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     type = models.CharField(max_length=20, choices=ALERT_TYPE_CHOICES)
#     is_read = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.user.username} - {self.type} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


# class Alert(models.Model):
#     alert_id = models.IntegerField()
#     # event_id =
#     user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     alert_type = models.CharField(max_length=50)
#     status = models.BooleanField()
#     send_at = models.DateTimeField(auto_now_add=True)

# class SMSAlert(models.Model):
#     ALERT_TYPE_CHOICES = [
#         ('fire', 'Fire'),
#         ('smoke', 'Smoke'),
#         ('system', 'System'),
#     ]

#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=20) 
#     alert_type = models.CharField(max_length=20, choices=ALERT_TYPE_CHOICES)
#     message = models.TextField()
#     location = models.CharField(max_length=255, blank=True)
#     sent_time = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='pending')  

#     def __str__(self):
#         return f"To {self.phone_number} | {self.alert_type.upper()} | {self.sent_time.strftime('%Y-%m-%d %H:%M')}"


