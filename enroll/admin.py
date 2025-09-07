from django.contrib import admin
from .models import Registration

# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display=['unique_id','name','gender','dob','city','district','pincode','state','country','email_id','otp']
admin.site.register(Registration,RegistrationAdmin)