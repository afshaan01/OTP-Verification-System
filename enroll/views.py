# from django.shortcuts import render,redirect
# from .models import Registration
# from django.db import IntegrityError
# import random
# from django.core.mail import send_mail
# from django.conf import settings


# from django.shortcuts import render, redirect
# from django.db import IntegrityError
# import random

# def registration(request):
#     context = {}

#     if request.method == 'POST':
#         try:
#             reg = Registration(
#                 unique_id=request.POST['unique_id'],
#                 name=request.POST['name'],
#                 gender=request.POST['gender'],
#                 dob=request.POST['dob'],
#                 city=request.POST['city'],
#                 district=request.POST['district'],
#                 pincode=request.POST['pincode'],
#                 state=request.POST['state'],
#                 country=request.POST['country'],
#                 email_id=request.POST['email_id'],
#             )
#             reg.save()
#             context['success'] = True
           
#             user_email_id = Registration.objects.get(email_id=reg.email_id)
#             print(user_email_id.email_id)

#             if user_email_id is not None:
#                 output = ""
#                 for i in range(1, 5):
#                     output += str(random.randint(0, 9))
#                 print(output)
#                 user_email_id.otp = output
                # user_email_id.save()

                # ✅ Redirect to send_random after saving and setting OTP
                # return redirect('send_random')  
            # <--- use URL name or path here

    #     except IntegrityError:
    #         context['error_msg'] = "Aadhar Number already exists."

    # return render(request, 'registration.html', context)














# def registration(request):
#     context = {}

#     if request.method == 'POST':
#         try:
#             reg = Registration(
#                 unique_id=request.POST['unique_id'],
#                 name=request.POST['name'],
#                 gender=request.POST['gender'],
#                 dob=request.POST['dob'],
#                 city=request.POST['city'],
#                 district=request.POST['district'],
#                 pincode=request.POST['pincode'],
#                 state=request.POST['state'],
#                 country=request.POST['country'],
#                 email_id=request.POST['email_id'],
#             )
#             reg.save()
#             context['success'] = True
           
#             user_email_id=Registration.objects.get(email_id=reg.email_id)
#             print(user_email_id.email_id)
#             if user_email_id is not None:
#                 output=""
#                 for i in range(1,5):
#                     output=output+str(random.randint(0,9))
#                 print(output)
#                 user_email_id.otp=output
#                 user_email_id.save()



#         except IntegrityError:
#             context['error_msg'] = "Aadhar Number already exists."

#     return render(request, 'registration.html', context)





# def send_random(request):
#     context = {}

#     if request.method == 'POST':
#         email=request.POST['email']
#         try:
#             email_matched=Registration.objects.get(email_id=email)
#             print(email_matched.otp)
#             fetched_otp=email_matched.otp
#             print(fetched_otp)
#             subject="OTP For Registration"
#             message=f"This is Your OTP {fetched_otp} for Login."
#             from_email=settings.EMAIL_HOST_USER
#             recipient_email=[email_matched.email_id]
#             send_mail(subject,message,from_email,recipient_email)

#             return redirect('match_otp')
        
#         except Registration.DoesNotExist:
            
#             context['error'] = "Email ID does not exist. Please try again."

    
#     return render(request,'input.html')



# def match_otp(request):
#     if request.method == 'POST':
#         entered_otp = request.POST['otp'].strip()  
#         try:
#             fetched = Registration.objects.get(otp=entered_otp)
#             existing_otp = fetched.otp
#             print(existing_otp)

#             if entered_otp == existing_otp:
#                 return render(request, 'match_otp.html', {'success': "OTP Verified!"})

#         except Exception:
#             return render(request, 'match_otp.html', {'error': "Invalid OTP"})

#     return render(request, 'match_otp.html')


# teh mera code tha pehle se likha hua 
# def match_otp(request):
#     if request.method == 'POST':
#         entered_otp=request.POST['otp'].strip()
#         entered_otp=int(entered_otp)
#         try:
#             fetched=Registration.objects.get(otp=entered_otp)
#             if entered_otp == fetched.otp:
#                  return redirect('registration')
#         except Registration.DoesNotExist:
#              pass  

#         return render(request, 'match_otp.html',{'error': 'Invalid OTP'})


    #         existing_otp=fetched.otp
    #         print(existing_otp)
      
    #         if entered_otp == existing_otp:
    #             return redirect('registration')
    #     except Exception:
    #         return render(request,'match_otp.html')
    # return render(request,'match_otp.html')




# def send_email():
#     subject="Welcome to Django Email Service"
#     message="This isa test email sent from Django."
#     from_email=settings.EMAIL_HOST_USER
#     recipient_list=['']
#     send_mail(subject,message,from_email,recipient_list)












































# from django.shortcuts import render
# from .models import Registration

# # Create your views here.
# def registration(request):

#     if request.method == 'POST':
#         unique=request.POST['unique_id']
#         name=request.POST['name']
#         gender=request.POST['gender']
#         dob=request.POST['dob']
#         city=request.POST['city']
#         district=request.POST['district']
#         pincode=request.POST['pincode']
#         state=request.POST['state']
#         country=request.POST['country']
#         email=request.POST['email_id']
      

#         reg=Registration(unique_id=unique,name=name,gender=gender,dob=dob,city=city,district=district,pincode=pincode,
#                     state=state,country=country,email_id=email)
#         reg.save()
    
#     return render(request,'registration.html')




# -------------------------------------------------------------------------------------------------------------------------------------------


from django.shortcuts import render,redirect
from .models import Registration
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
def registration(request):
    if request.method == 'POST':
        u_id=request.POST.get('u_id')
        u_name=request.POST['name']
        u_gender=request.POST['gender']
        u_dob=request.POST['dob']
        u_country=request.POST['country']
        u_state=request.POST['state']
        u_city=request.POST['city']
        u_district=request.POST['district']
        u_pincode=request.POST['pincode']
        u_email=request.POST['email_id']
        reg=Registration(unique_id=u_id,name=u_name,gender=u_gender,dob=u_dob,country=u_country,state=u_state,
                     city=u_city,district=u_district,pincode=u_pincode,email_id=u_email)
        reg.save()
        user_email_id=Registration.objects.get(email_id=reg.email_id)
        print(user_email_id.email_id)
        if user_email_id is not None:
            output=""
            for i in range(1,5):
                output=output+str(random.randint(0,9))
            print(output)
            user_email_id.otp=output
            user_email_id.save()
        return redirect('send_random') 
          
    return render(request,'registration.html')


def send_random(request):
    if request.method == 'POST':
        email=request.POST['email']
        try:
            email_matched=Registration.objects.get(email_id=email)
            print(email_matched.otp)
            fetched_otp=email_matched.otp
            print(fetched_otp)
            subject="OTP For Registration"
            message=f"This is your otp {fetched_otp} for Login"
            from_email=settings.EMAIL_HOST_USER
            recipient_list=[email_matched.email_id]
            send_mail(subject,message,from_email,recipient_list)
            
            
        except Exception:
            print("does not matched")
        return redirect('match_otp')
    
    return render(request,'input.html')

# def match_otp(request):
#     if request.method == 'POST':
#         entered_otp=request.POST['otp']
#         entered_otp=int(entered_otp)
#         try:
    
#             fetched=Registration.objects.get(otp=entered_otp)
#             existing_otp=fetched.otp
#             print(existing_otp)
#             if entered_otp==fetched.otp:
#                print('yes')
#                return redirect('home')
#         except Exception:
#             print('no')
#             return render(request,'match_otp.html')
    
#     return render(request,'match_otp.html')








# def match_otp(request):
#     if request.method == 'POST':
#         entered_otp = request.POST['otp']
#         print(entered_otp)
#         try:
#             fetched = Registration.objects.get(otp=entered_otp)
#             existing_otp = fetched.otp
#             print(existing_otp)
#             if entered_otp == fetched.otp:
#                 print('yes')
#                 return redirect('home')
#             else:
#                 print('no')
#                 return render(request, 'match_otp.html')
#         except Exception:
#             print('no')
#             return render(request, 'match_otp.html')
    
#     return render(request, 'match_otp.html')


def match_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST['otp']
        print("Form se aaya OTP:", repr(entered_otp), type(entered_otp))

        try:
            fetched = Registration.objects.filter(otp=entered_otp).last()
            if fetched is not None:
                print("DB OTP:", repr(fetched.otp), type(fetched.otp))
                if str(entered_otp).strip() == str(fetched.otp).strip():
                    print('yes')
                    return redirect('registration')
            print('no')
            return render(request, 'match_otp.html')

        except Exception as e:
            print("Exception:", str(e))
            return render(request, 'match_otp.html')

    return render(request, 'match_otp.html')

