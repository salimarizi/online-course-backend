from django.contrib import admin
from .models import Course, Syllabus, Project

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['title', 'description', 'career_path']
    
admin.site.register(Course, CourseAdmin)

class SyllabusAdmin(admin.ModelAdmin):
    model = Syllabus
    list_display = ['title', 'get_course', 'description']
    
    @admin.display(ordering='course__title', description='Course Title')
    def get_course(self, obj):
        return obj.course.title
    
admin.site.register(Syllabus, SyllabusAdmin)

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['title', 'get_course', 'description']
    
    @admin.display(ordering='course__title', description='Course Title')
    def get_course(self, obj):
        return obj.course.title
    
admin.site.register(Project, ProjectAdmin)