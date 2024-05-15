from rest_framework import serializers

from task.models import TaskModel


class TaskListSerializer(serializers.ModelSerializer):
    project_title = serializers.CharField(source='project.title', read_only=True)
    developer_first_name = serializers.CharField(source='developer.first_name', read_only=True)
    developer_last_name = serializers.CharField(source='developer.last_name', read_only=True)
    developer_email = serializers.CharField(source='developer.email', read_only=True)
    developer_profile_picture = serializers.CharField(source='developer.profile_picture', read_only=True)
    class Meta:
        model = TaskModel
        fields = [
            "id",
            "title",
            "project",
            "project_title",
            "developer",
            "developer_first_name",
            "developer_last_name",
            "developer_email",
            "developer_profile_picture",
            "description",
            "requirements",
            "deadline",
            "is_complete",
            "is_active",
            ]
