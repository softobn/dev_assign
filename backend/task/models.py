from django.db import models

from utils.models import CommonInfo
from project.models import ProjectModel


class TaskModel(CommonInfo):
    title = models.CharField(max_length=100)
    project = models.ForeignKey(ProjectModel, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200)
    requirements = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.project.title} : {self.title}"

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        db_table = "task"
