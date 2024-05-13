from rest_framework.serializers import ModelSerializer

from project.models import ProjectModel


class ManagerCreateProjectSerializer(ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = [
            "id",
            "title",
            "manager",
            "description",
            "requirements",
            "thumbnail",
            "images",
            "planned_start",
            "planned_end",
            "deadline",
            "is_complete",
            "is_active",
            ]
