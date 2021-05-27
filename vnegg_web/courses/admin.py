from django.contrib import admin

# Register your models here.
from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'educator', 'num_lessons')
    search_fields = ('name',)

admin.site.register(Course, CourseAdmin )