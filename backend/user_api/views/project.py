from django.shortcuts import get_list_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from project.models import ProjectModel
from ..serializers.project import ProjectListSerializer


class ProjectListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        manager_id = request.query_params.get("manager_id")
        is_active = request.query_params.get("is_active")
        if manager_id:
            projects = ProjectModel.objects.filter(manager__id=manager_id)
            serializer = ProjectListSerializer(projects, many=True)        
            return Response(serializer.data)
        if is_active:
            projects = ProjectModel.objects.filter(is_active=is_active)
            serializer = ProjectListSerializer(projects, many=True)        
            return Response(serializer.data)
        projects = get_list_or_404(ProjectModel, is_active=True)
        serializer = ProjectListSerializer(projects, many=True)        
        return Response(serializer.data)


class ProjectDoneView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        projects = ProjectModel.objects.filter(is_complete=True, is_active=True)
        counted = projects.count()        
        return Response({"done": counted})


class ProjectInprocessView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        projects = ProjectModel.objects.filter(is_complete=False, is_active=True)
        counted = projects.count()        
        return Response({"inprocess": counted})


class ProjectCreatedCountView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        projects = ProjectModel.objects.filter()
        counted = projects.count()        
        return Response({"created": counted})
