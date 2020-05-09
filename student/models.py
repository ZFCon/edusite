from django.db import models
from school.models import School 
from department.models import Department
from dptclass.models import DptClass

class Student(models.Model):
    student_id = models.OneToOneField('account.Student', on_delete=models.CASCADE)
    course    = models.ManyToManyField('course.Course', null=True, blank=True, related_name="sc_crse_reg")  

    def get_absolute_url(self):
        return reverse('student-detail-view', args=[str(self.student_id)])

    def __str__(self):
        return str(self.student_id) 


class SCRecord(models.Model):
    student  = models.ForeignKey('account.Student', on_delete=models.CASCADE)
    course   = models.ManyToManyField('course.Course', related_name="screcord")
    caone    = models.IntegerField()
    catwo    = models.IntegerField()
    midterm  = models.IntegerField()
    cathree  = models.IntegerField()
    cafour   = models.IntegerField()
    project  = models.IntegerField()
    exam     = models.IntegerField()
    total    = models.IntegerField()
    grade    = models.CharField(max_length=20)

    def __str__(self):
        return str(self.student)

    