from django.db import models
from django.conf import settings


class Section(models.Model):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return 'Section: ' + self.name


class Course(models.Model):
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return 'Course: ' + self.name
