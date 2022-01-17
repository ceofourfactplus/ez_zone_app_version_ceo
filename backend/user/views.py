from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str,force_text,DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings

# def send_action_email(user,request):
#     current_site = get_current_site(request)
#     email_sujects = 'Activate your account'
#     email_body = render_to_string('user/activate.html',{
#         'user':user,
#         'domain':current_site,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': generate_token.make_token(user )
#     })

#     email = EmailMessage(subject=email_sujects,body=email_body,from_email=settings.EMAIL_FROM_USER,to=[user.email])
#     email.send() 

# def activate_user(request,uidb64,token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(id=uid)
#     except Exception as e:
#         user=None

#     if  user and generate_token.check_token(user,token):
#         user.is_email_verified = True
#         user.save()
#         return Response('email is verified already')

#     return Response(request,user)

class RegisterUserAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        is_pos_user = request.data['is_pos_user']
        print(request.data)
        print(username)
        can_save = True

        
        if User.objects.filter(username=username).exists():
            self.can_save = False
            return Response('Username is taken, choose another one', status=400)

        if User.objects.filter(email=email).exists():
            self.can_save = False
            return Response('Username is taken, choose another one', status=400)

        if can_save:
            user = User.objects.create_user(username=username,email=email,password=password,is_pos_user=is_pos_user)
            user.first_name = request.data["first_name"]
            user.last_name = request.data["last_name"]
            user.save()
            return Response("created") 
        
        return Response("created")   


class UserInfo(APIView):
    def get(self, request):
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "first_name":request.user.first_name,
            "last_name":request.user.last_name
        })
