from django.contrib import admin
from . import models


admin.site.register(models.Course)
admin.site.register(models.CourseStudent)
admin.site.register(models.CourseTeacher) 
admin.site.register(models.CourseSRecord)
