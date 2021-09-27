from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication

class UserInfo (APIView):
    def get(self, request):
        print(request.user.id)
        return Response({
            "id": request.user.id,
            "name": request.user.username,
            "email": request.user.email
        })
