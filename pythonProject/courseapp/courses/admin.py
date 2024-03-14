from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Course


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['name']
    list_filter = ['id', 'name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description', 'category', 'created_date', 'updated_date', 'active']
    search_fields = ['subject']
    list_filter = ['id', 'subject', 'category']
    readonly_fields = ['avatar']

    def avatar(self, course):
        if course:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=course.image.name)
            )


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
