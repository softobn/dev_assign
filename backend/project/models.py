from django.db import models

from utils.models import CommonInfo
from user.models import UserAccount


class ProjectModel(CommonInfo):
    title = models.CharField(max_length=100)
    manager = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200)
    requirements = models.TextField()
    thumbnail = models.URLField(null=True, blank=True)
    images = models.JSONField(null=True, blank=True)
    planned_start = models.DateField(null=True, blank=True)
    planned_end = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.manager} : {self.title}"

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        db_table = "project"
