from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Attendance(models.Model):
    user = models.CharField(max_length=30)
    checkinn = models.TimeField(null=True, blank=True)
    checkout = models.TimeField(null=True, blank=True)
    date = models.DateField()
    worked_for = models.CharField(max_length=100, null=True, blank=True)
    extended1 = models.CharField(max_length=100, null=True, blank=True)
    early = models.CharField(max_length=100, null=True, blank=True)

    created_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=200)
    modified_by = models.DateField(blank=True, null=True)
    modified_on = models.DateField(blank=True, null=True)
    is_actve = models.BooleanField(default=False)
    url = models.URLField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return str(self.id)
