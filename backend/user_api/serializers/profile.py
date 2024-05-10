from rest_framework.serializers import ModelSerializer

from user.models import UserAccount


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            "id",
            "phone_number",
            "email",
            "first_name",
            "last_name",
            "gender",
            "religion",
            "date_of_birth",
            "area",
            "address",
            "marital_status",
            "profile_picture",
            "total_project",
            ]
