from django.db import models
from account.models import Student
from course.models import Course

class SRecord(models.Model):
    ASSESSMENT_TYPES = [
        ('PR', 'Project Report'),
        ('CA1', 'Continuous Assessment 1'),
        ('CA2', 'Continuous Assessment 2'),
        ('MT', 'MidTerm Exam'), 
        ('CA3', 'Continuous Assessment 3'),
        ('CA4', 'Continuous Assessment 4'),
        ('FE', 'Final Exam'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    astype = models.CharField(
        max_length=10,
        choices=ASSESSMENT_TYPES,
    )
    score = models.IntegerField()
    grade = models.CharField(max_length=20)

    def __str__(self):
        return str(self.student)

class SCourse(models.Model):
    srecord = models.ForeignKey(SRecord, on_delete=models.CASCADE)
    scourse = models.ForeignKey(Course, on_delete=models.CASCADE)