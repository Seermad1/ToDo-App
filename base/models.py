from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    avatar = models.ImageField(null=True, default="avatar.svg", upload_to="images/")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated","-created"] 

    def __str__(self):
        return self.title
