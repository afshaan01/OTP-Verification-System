from django.urls import path
from .import views

urlpatterns=[
    path('',views.registration,name="registration"),
    path('send_randoms/',views.send_random,name="send_random"),
    path('match_otp/',views.match_otp,name="match_otp"),

   
]