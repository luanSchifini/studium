from django.db import models

from django.db import models
from django.utils import timezone
import datetime

class Student(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    subject = models.CharField(max_length=200)
    grade = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    realized_at = models.DateTimeField("date of the assignment")

    def __str__(self):
        return self.subject

    def was_realized_recently(self):
        return self.realized_at >= timezone.now() - datetime.timedelta(days=60)

# Create your models here.
