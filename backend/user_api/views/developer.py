from django.contrib.auth.hashers import make_password

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from user.models import UserAccount
from ..serializers.developer import DeveloperRegisterSerializer


class DeveloperRegisterView(APIView):
    permission_classes = [AllowAny]

    def validate_parameter(self, phone_number, email, password):
        if phone_number and email and password:
            return True
        else:
            return False

    def post(self, request):
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")
        password = request.data.get("password")

        if self.validate_parameter(phone_number, email, password) is True:

            data = request.data.copy()
            data["password"] = make_password(password)

            serializer = DeveloperRegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("success")
            
        return Response("unsuccess")


class DeveloperListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        developers = UserAccount.objects.filter(is_manager=False)
        serializer = DeveloperRegisterSerializer(developers, many=True)
        return Response(serializer.data)
