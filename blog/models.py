from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    #year_of_recording = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.first_name
# Create your models here.
