from django.db import models


class Registration(models.Model):
    unique_id=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    gender=models.CharField(max_length=1,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    district=models.CharField(max_length=50,null=True,blank=True)
    pincode=models.CharField(max_length=20,null=True,blank=True)
    state=models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    otp=models.IntegerField(null=True,blank=True)
    email_id=models.EmailField(max_length=50,null=True,blank=True)
    current_date_timestamp=models.DateTimeField(auto_now=True,null=True,blank=True)
