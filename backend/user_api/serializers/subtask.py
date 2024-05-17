from rest_framework import serializers

from task.models import TaskModel


class SubTaskListSerializer(serializers.ModelSerializer):
    task_title = serializers.CharField(source='task.title', read_only=True)
    task_id = serializers.CharField(source='task.id', read_only=True)
    developer_email = serializers.CharField(source='task.developer.email', read_only=True)
    class Meta:
        model = TaskModel
        fields = [
            "id",
            "title",
            "task_id",
            "task_title",
            "developer_email",
            "description",
            "requirements",
            "deadline",
            "is_complete",
            ]
