from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.safestring import mark_safe

from .models import Category, Course


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['name']
    list_filter = ['id', 'name']


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'created_date', 'updated_date', 'active']
    search_fields = ['subject']
    list_filter = ['id', 'name', 'category']
    form = CourseForm
    # inlines = [CategoryInlineAdmin]
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.image.name)
            )


# class CourseAppAdminSite(admin.AdminSite):
#     site_header = 'My App'
#
#     def get_urls(self):
#         return [
#             path('course-stats/', self.stats_view)
#         ] + super().get_urls()
#
#     def stats_view(self, request):
#         return TemplateResponse(request, 'admin/stats.html', {
#             'stats': dao.count_courses_by_cate()
#         })
#
#
# admin_site = CourseAppAdminSite(name='myapp')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
