from datetime import datetime

from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from user.models import UserAccount
from project.models import ProjectModel
from task.models import TaskModel
from utils.utils import tokenValidation
from ..serializers.project import ManagerCreateProjectSerializer


class ManagerCreateProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        manager = tokenValidation(request)["id"]
        data["manager"] = manager
        serializer = ManagerCreateProjectSerializer(data=data)
        manager = get_object_or_404(UserAccount, id=manager)
        manager.total_project += 1
        manager.save()
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        
        return Response("unsuccess")


class ManagerUpdateProjectView(APIView):
    permission_classes = [AllowAny]

    def validate_parameter(self, project_id):
        return project_id is not None

    def patch(self, request):
        project_id = request.data.get("project_id")
        if self.validate_parameter(project_id) is True:
            project = get_object_or_404(ProjectModel, id=project_id)
            serializer = ManagerCreateProjectSerializer(instance=project, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response("success")
            else:
                return Response(serializer.errors)
        
        return Response("unsuccess")


class ManagerMarkprojectView(APIView):
    permission_classes = [AllowAny]

    def validate_parameter(self, project_id):
        return project_id is not None
    
    def taskComplete(self, id):
        tasks = TaskModel.objects.filter(project__id=id)
        task_counts = tasks.aggregate(
            total_tasks=Count('id'),
            complete_tasks=Count('id', filter=Q(is_complete=True))
        )

        all_complete = task_counts['total_tasks'] == task_counts['complete_tasks']
        return all_complete

    def patch(self, request):
        project_id = request.data.get("project_id")
        if self.validate_parameter(project_id) is True:
            project = get_object_or_404(ProjectModel, id=project_id)
            if project.deadline >= datetime.now().date() and self.taskComplete(project_id) is True:
                project.is_complete = True
                project.is_active = False
                project.save()
                return Response("success")
            elif self.taskComplete(project_id) is True:
                project.is_complete = True
                project.save()
                return Response("success")
        
        return Response("unsuccess")
