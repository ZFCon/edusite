from django.db import models
from account.models import Teacher
from course.models import Course



class TRecord(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, through='TCourse')
    score = models.IntegerField()
    grade = models.CharField(max_length=20)

    def __str__(self):
        return str(self.teacher_id)

class TCourse(models.Model):
    trecord = models.ForeignKey(TRecord, on_delete=models.CASCADE)
    tcourse = models.ForeignKey(Course, on_delete=models.CASCADE)