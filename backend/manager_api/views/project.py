from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import UserAccount
from project.models import ProjectModel
from utils.custom_permission import IsManager
from utils.utils import tokenValidation
from ..serializers.project import ManagerCreateProjectSerializer


class ManagerCreateProjectView(APIView):
    permission_classes = [IsManager]

    def post(self, request):
        serializer = ManagerCreateProjectSerializer(data=request.data)
        manager = get_object_or_404(UserAccount, id=tokenValidation(request)["id"])
        manager.total_project += 1
        manager.save()
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        
        return Response("unsuccess")


class ManagerUpdateProjectView(APIView):
    permission_classes = [IsManager]

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
