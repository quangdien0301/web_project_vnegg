from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(default='', max_length=255)
    educator = models.CharField(default='', max_length=100)
    description = models.TextField(default='', max_length=1000)
    excerpt = models.TextField(default='', max_length=300)
    num_lessons = models.PositiveSmallIntegerField(default=0)
    picture = models.ImageField(upload_to='course_picture')

    def __str__(self):
        return self.name

