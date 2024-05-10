from datetime import datetime

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["id"] = user.id
        token["phone_number"] = user.phone_number
        token["email"] = user.email
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["is_staff"] = user.is_staff
        token["is_manager"] = user.is_manager
        token["current_date"] = datetime.now().strftime("%Y:%m:%d")
        current_time = datetime.now().strftime("%I:%M:%p")
        token["current_time"] = current_time

        if "AM" in current_time:
            token["day_status"] = "Day"
        else:
            token["day_status"] = "Night"

        token["location"] = "Dhaka"

        return token
