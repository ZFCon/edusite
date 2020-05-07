from django.db import models

from department.models import Department  


def upload_location(instance, filename):
	file_path = 'book/{bk_id}/{title}-{filename}'.format(
				bk_id=str(instance.bk_id),bk_title=str(instance.bk_title), filename=filename)
	return file_path

class Book(models.Model):
    bk_dpt = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    #bk_code = models.PositiveSmallIntegerField(unique=True, null=True)
    bk_title = models.CharField(max_length=50, null=False, blank=False)
    bk_cover = models.ImageField(upload_to=upload_location, null=True, blank=True)
    bk_file = models.FileField(upload_to=upload_location, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('book-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.bk_title)
