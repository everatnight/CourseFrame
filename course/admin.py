from django.contrib import admin
from course.models import teacher, resources, assignment, announcement, course, textbook


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'rtype', 'filename', 'assignment', 'timestamp')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'researcharea', 'biography', 'contact', 'officehour', 'picture', 'project')
    ordering = ('name',)

admin.site.register(teacher, TeacherAdmin)
admin.site.register(resources, ResourceAdmin)
admin.site.register(assignment)
admin.site.register(announcement)
admin.site.register(course)
admin.site.register(textbook)
