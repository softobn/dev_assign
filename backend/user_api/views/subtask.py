from django.shortcuts import get_list_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from subtask.models import SubTaskModel
from ..serializers.subtask import SubTaskListSerializer


class SubTaskListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        task_id = request.query_params.get("task_id")
        if task_id:
            subtasks = SubTaskModel.objects.filter(task__id=task_id)
            serializer = SubTaskListSerializer(subtasks, many=True)        
            return Response(serializer.data)

        subtasks = get_list_or_404(SubTaskModel, is_active=True)
        serializer = SubTaskListSerializer(subtasks, many=True)        
        return Response(serializer.data)
