from rest_framework.serializers import ModelSerializer

from task.models import TaskModel


class TaskListSerializer(ModelSerializer):
    class Meta:
        model = TaskModel
        fields = [
            "id",
            "title",
            "project",
            "developer",
            "description",
            "requirements",
            "deadline",
            "is_complete",
            ]
