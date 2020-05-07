from django.db import models
from django.conf import settings
from institute.models import Institute


class School(models.Model):
    sch_abb = models.CharField(max_length=20, default='None')
    #sch_code = models.PositiveSmallIntegerField(unique=True, blank=True)
    sch_name = models.CharField(max_length=100)
    sch_inst = models.ForeignKey(Institute, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('school-detail-view', args=[str(self.sch_code)])

    def __str__(self):
        return str(self.sch_name)

