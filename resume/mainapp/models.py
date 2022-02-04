from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length= 1500)
    images = models.ImageField(upload_to = 'resume/image')
    url = models.URLField(blank=True)

def __self__(self):
    return self.title