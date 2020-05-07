from django.db import models

from department.models import Department  


class DptClass(models.Model):
    dcls_dpt = models.ForeignKey(Department, on_delete=models.CASCADE)
    dcls_abb = models.CharField(max_length=20, default='None')
    #dcls_code = models.PositiveSmallIntegerField(unique=True, blank=True)
    dcls_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('dptclass-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.dcls_name)
