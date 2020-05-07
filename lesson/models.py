from django.db import models
from course.models import Course

def upload_location(instance, filename):
	file_path = 'lsnnote/{le_note}-{filename}'.format(
				le_note=str(instance.le_note), filename=filename)
	return file_path

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    le_name = models.CharField(max_length=100)
    #le_code = models.PositiveSmallIntegerField(unique=True, blank=True)
    le_note = models.FileField(upload_to=upload_location, null=True, blank=True)
    le_video = models.CharField(max_length=100, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('lesson-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.le_name)