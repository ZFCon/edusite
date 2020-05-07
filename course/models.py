from django.db import models

from dptclass.models import DptClass
from student.models import Student, SCRecord
from teacher.models import Teacher

 
class Course(models.Model):
    ce_dptcls = models.ForeignKey(DptClass, on_delete=models.CASCADE)
    #ce_code = models.PositiveSmallIntegerField(unique=True, blank=True)
    ce_abb = models.CharField(max_length=20, unique=True, default='None') 
    ce_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('course-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.ce_name)

class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)

    def get_absolute_url(self):
        return reverse('cstudent-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.course)

class CourseTeacher(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher)

    def get_absolute_url(self):
        return reverse('cteacher-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.course)

class CourseSRecord(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    screcord = models.ManyToManyField(SCRecord)

    def get_absolute_url(self):
        return reverse('csrecord-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.course)


