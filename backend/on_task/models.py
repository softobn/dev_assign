from django.db import models

from utils.models import CommonInfo
from project.models import ProjectModel
from user.models import UserAccount


class OnTaskModel(CommonInfo):
    project = models.ForeignKey(ProjectModel, on_delete=models.DO_NOTHING)
    developer = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.project} : {self.developer}"

    class Meta:
        verbose_name = "On Task"
        verbose_name_plural = "On Tasks"
        db_table = "on_task"
