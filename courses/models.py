from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract: True

    subject = models.CharField(max_length=255, null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return self.subject


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m')

    def __str__(self):
        return self.username


class Category(models.Model):
    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    parent_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    class Meta:
        ordering = ["subject"]

    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class Lesson(BaseModel):
    content = models.TextField(null=True, blank=True)
    courses = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField("Tag", blank=False)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
