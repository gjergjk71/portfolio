from django.db import models

# Create your models here.

class Module(models.Model):
	name = models.CharField(max_length=500)
	duration = models.DateTimeField()
	description = models.TextField()
	status = models.BooleanField()
	def __str__(self):
		pass