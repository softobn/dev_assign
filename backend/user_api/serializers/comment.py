from rest_framework.serializers import ModelSerializer

from comment.models import CommentModel


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        fields = [
            "id",
            "user",
            "reply",
            "task",
            "subtask",
            ]

class CommentListSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        fields = [
            "id",
            "user",
            "reply",
            ]

