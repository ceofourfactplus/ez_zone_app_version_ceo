from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response



class RegisterUserAPIView(APIView):
    def post(self, request):
        user_name = request.data['username']
        email = request.data['email']
        password = request.data['password']
        print(request.data)
        print(user_name)
        
        user = User.objects.create_user(username=user_name,email=email,password=password)
        # user = user.save(commit=False)
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.save()
        # print(user)
        # data = {
        #     "id" : user["id"],
        #     "username" : user["username"],
        #     "email" : user["email"],
        #     "frist_name" : user["first_name"],
        #     "last_name" : user["last_name"],
        # }
        return Response("ok")   


class UserInfo(APIView):
    def get(self, request):
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "first_name":request.user.first_name,
            "last_name":request.user.last_name
        })
