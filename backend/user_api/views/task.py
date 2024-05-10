from django.shortcuts import get_list_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from task.models import TaskModel
from ..serializers.task import TaskListSerializer


class TaskListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        project_id = request.query_params.get("project_id")
        if project_id:
            tasks = TaskModel.objects.filter(project__id=project_id)
            serializer = TaskListSerializer(tasks, many=True)        
            return Response(serializer.data)

        tasks = get_list_or_404(TaskModel, is_active=True)
        serializer = TaskListSerializer(tasks, many=True)        
        return Response(serializer.data)
