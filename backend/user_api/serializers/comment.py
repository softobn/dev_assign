from rest_framework import serializers

from comment.models import CommentModel


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = [
            "id",
            "user",
            "reply",
            "task",
            "subtask",
            ]

class CommentListSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='user.email', read_only=True)
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)
    user_picture = serializers.CharField(source='user.profile_picture', read_only=True)
    class Meta:
        model = CommentModel
        fields = [
            "id",
            "user_email",
            "user_first_name",
            "user_picture",
            "reply",
            ]

