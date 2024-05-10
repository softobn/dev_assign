from django.shortcuts import get_list_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from comment.models import CommentModel
from utils.utils import tokenValidation
from ..serializers.comment import CommentCreateSerializer, CommentListSerializer


class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id=tokenValidation(request)["id"]
        data = request.data.copy()
        data["user"] = user_id
        serializer = CommentCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        
        return Response("unsuccess")


class CommentListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        task_id = request.query_params.get("task_id")
        subtask_id = request.query_params.get("subtask_id")

        if subtask_id:
            comments = CommentModel.objects.filter(subtask__id=subtask_id)
            serializer = CommentListSerializer(comments, many=True)        
            return Response(serializer.data)
        if task_id:
            comments = CommentModel.objects.filter(task__id=task_id)
            serializer = CommentListSerializer(comments, many=True)        
            return Response(serializer.data)

        comments = get_list_or_404(CommentModel)
        serializer = CommentListSerializer(comments, many=True)        
        return Response(serializer.data)
