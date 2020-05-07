from django.db import models

from course.models import Course
from student.models import SCRecord
 
class CSRecord(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ManyToManyField(SCRecord)

    def get_absolute_url(self):
        return reverse('course-record-view', args=[str(self.id)])

    def __str__(self):
        return str(self.course)

