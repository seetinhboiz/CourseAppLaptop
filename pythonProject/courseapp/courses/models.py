from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Course(BaseModel):
    name = models.CharField(max_length=255, null=True)
    description = RichTextField()
    image = CloudinaryField(null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_query_name="courses")


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = CloudinaryField()
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.subject