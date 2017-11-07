from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Profile(models.Model):
	fname = models.CharField(max_length=125, default="")
	lname = models.CharField(max_length=125, null=True)
	description = models.TextField(null=True)

	def __str__(self):
		return self.fname + " " + self.lname
