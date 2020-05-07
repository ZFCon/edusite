from django.db import models


class Institute(models.Model): 
    abb = models.CharField(max_length=20, default='None')
    #code = models.PositiveSmallIntegerField(unique=True, blank=True)
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('institute-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.name)

