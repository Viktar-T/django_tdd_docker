from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Movies(models.Model):
    # employees = models.ManyToManyField(Employee, related_name="employee_list", blank=True)
    title = models.CharField(max_length=50, default="empty")
    genre = models.CharField(max_length=50, default="empty")
    year = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

