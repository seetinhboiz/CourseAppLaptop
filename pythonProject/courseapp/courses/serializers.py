from rest_framework import serializers
from .models import Category, Course, Tag, Lesson


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TagSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        req = super().to_representation(instance)
        req['image'] = instance.image.url
        return req


class LessonSerializer(ItemSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'created_date']