from django.db import models

from utils.models import CommonInfo
from task.models import TaskModel


class SubTaskModel(CommonInfo):
    title = models.CharField(max_length=100)
    task = models.ForeignKey(TaskModel, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200)
    requirements = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.task.title} : {self.title}"

    class Meta:
        verbose_name = "Sub Task"
        verbose_name_plural = "Sub Tasks"
        db_table = "subtask"
