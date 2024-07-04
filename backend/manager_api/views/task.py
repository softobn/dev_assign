from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from task.models import TaskModel
from ..serializers.task import ManagerCreateTaskSerializer


class ManagerCreateTaskView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ManagerCreateTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        
        return Response("unsuccess")


class ManagerUpdateTaskView(APIView):
    permission_classes = [AllowAny]

    def validate_parameter(self, task_id):
        return task_id is not None

    def patch(self, request):
        task_id = request.data.get("task_id")
        if self.validate_parameter(task_id) is True:
            task = get_object_or_404(TaskModel, id=task_id)
            serializer = ManagerCreateTaskSerializer(instance=task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response("success")
        
        return Response("unsuccess")
