from django.db import models
from course.models import Course
from question.models import Question

class Assessment(models.Model):
    ASSESSMENT_TYPES = [
        ('PR', 'Project Report'),
        ('HW', 'Home Work'),
        ('CA1', 'Continuous Assessment 1'),
        ('CA2', 'Continuous Assessment 2'),
        ('MT', 'MidTerm Exam'),
        ('CA3', 'Continuous Assessment 3'),
        ('CA4', 'Continuous Assessment 4'),
        ('FE', 'Final Exam'),
    ]
    as_type = models.CharField(
        max_length=10,
        choices=ASSESSMENT_TYPES,
    )
    as_ce = models.ForeignKey(Course, on_delete=models.CASCADE)
    as_name = models.CharField(max_length=100)
    # question = models.ManyToManyField('question.Question', related_name="as_qtn_reg")
    
    def get_absolute_url(self):
        return reverse('assessment-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.as_name)


class AssQuestion(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question = models.ManyToManyField(Question)

    def get_absolute_url(self):
        return reverse('aquestion-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.assessment)

    
