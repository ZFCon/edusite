from django.db import models

from school.models import School


class Department(models.Model):
    dpt_sch = models.ForeignKey(School, on_delete=models.CASCADE)
    dpt_abb = models.CharField(max_length=20, default='None')
    #dpt_code = models.PositiveSmallIntegerField(unique=True, blank=True)
    dpt_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('department-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.dpt_name)

