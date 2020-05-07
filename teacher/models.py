from django.db import models
from account.models import Teacher
from school.models import School
from department.models import Department
from dptclass.models import DptClass
from course.models import Course


class Teacher(models.Model):
    teacher_id      = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    school          = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True) 
    course          = models.ManyToManyField('course.Course', related_name="tc_crse_reg")

    def get_absolute_url(self):
        return reverse('teacher-detail-view', args=[str(self.teacher_id)])

    def __str__(self):
        return str(self.teacher_id) 


class TCRecord(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ManyToManyField('course.Course', related_name='tcrecord')
    engagement = models.IntegerField()

    def __str__(self):
        return str(self.teacher)


