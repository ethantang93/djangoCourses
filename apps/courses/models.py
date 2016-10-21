from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table='courses'
