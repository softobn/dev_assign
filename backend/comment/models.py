from django.db import models

from utils.models import CommonInfo
from user.models import UserAccount
from task.models import TaskModel
from subtask.models import SubTaskModel


class CommentModel(CommonInfo):
    user = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    reply = models.CharField(max_length=100)
    task = models.ForeignKey(TaskModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    subtask = models.ForeignKey(SubTaskModel, on_delete=models.DO_NOTHING, null=True, blank=True)


    def __str__(self):
        return f"{self.user.email} : {self.reply}"

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
        db_table = "comment"
