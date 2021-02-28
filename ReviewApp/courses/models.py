from django.db import models

# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return 'Section: ' + self.name


class Course(models.Model):
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    name = models.CharField(max_length=80)

    def __str__(self):
        return 'Course: ' + self.name
