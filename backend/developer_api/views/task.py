from datetime import datetime

from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from task.models import TaskModel


class DeveloperMarkTaskView(APIView):
    permission_classes = [AllowAny]

    def validate_parameter(self, task_id):
        return task_id is not None

    def patch(self, request):
        task_id = request.data.get("task_id")
        if self.validate_parameter(task_id) is True:
            task = get_object_or_404(TaskModel, id=task_id)
            if task.deadline >= datetime.now().date():
                task.is_complete = True
                task.is_active = False
                task.save()
                return Response("success")
            else:
                task.is_complete = True
                task.save()
                return Response("success")

        
        return Response("unsuccess")
