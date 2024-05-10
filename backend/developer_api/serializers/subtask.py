from rest_framework import serializers

from subtask.models import SubTaskModel


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTaskModel
        fields = [
            "id",
            "title",
            "task",
            "description",
            "requirements",
            "deadline",
            ]
