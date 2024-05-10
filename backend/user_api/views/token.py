from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers.token import CustomTokenSerializer


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

    def validate_parameter(self, email, password):
        if email and password:
            return True
        else:
            return False

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        if self.validate_parameter(email, password) is True:
            response = super().post(request, *args, **kwargs)
            access_token = str(response.data["access"])
            refresh_token = str(response.data["refresh"])

            token_data = {
                "access": access_token,
                "refresh": refresh_token,
            }

            token = access_token
            request.session["token"] = token

            return Response(token_data)
        
        return Response("unsuccess")
