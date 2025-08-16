from django.contrib import admin
from .models import Company, UserProfile
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Company)

# Username : firemonitoring
# Email address: firemonitoring@gmail.com
# password : 12345