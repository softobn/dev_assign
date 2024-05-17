from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from subtask.models import SubTaskModel
from utils.custom_permission import IsDeveloper
from ..serializers.subtask import SubTaskCreateSerializer


class DeveloperCreateSubTaskView(APIView):
    permission_classes = [IsDeveloper]

    def post(self, request):
        serializer = SubTaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        
        return Response("unsuccess")


class DeveloperUpdateSubTaskView(APIView):
    permission_classes = [IsDeveloper]

    def validate_parameter(self, subtask_id):
        return subtask_id is not None

    def patch(self, request):
        subtask_id = request.data.get("subtask_id")
        if self.validate_parameter(subtask_id) is True:
            subtask = get_object_or_404(SubTaskModel, id=subtask_id)
            serializer = SubTaskCreateSerializer(instance=subtask, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response("success")
        
        return Response("unsuccess")


class DeveloperMarkSubTaskView(APIView):
    permission_classes = [IsDeveloper]

    def validate_parameter(self, subtask_id):
        return subtask_id is not None

    def patch(self, request):
        subtask_id = request.data.get("subtask_id")
        if self.validate_parameter(subtask_id) is True:
            subtask = get_object_or_404(SubTaskModel, id=subtask_id)
            subtask.is_complete = True
            subtask.save()
            return Response("success")
        
        return Response("unsuccess")
