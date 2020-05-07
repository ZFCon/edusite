from django.db import models
from course.models import Course 

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  
    #qtn_code = models.PositiveSmallIntegerField(unique=True)
    qtn = models.CharField(max_length=100, blank=True)
    qtn_ans = models.CharField(max_length=100, blank=True)
    qtn_opta = models.CharField(max_length=100, blank=True)
    qtn_optb = models.CharField(max_length=100, blank=True)
    qtn_optc = models.CharField(max_length=100, blank=True)
    qtn_optd = models.CharField(max_length=100, blank=True)
    qtn_opte = models.CharField(max_length=100, blank=True)
    assessment = models.ManyToManyField('assessment.Assessment', related_name="qtn_reg")

    def get_absolute_url(self):
        return reverse('assessment-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.qtn)
