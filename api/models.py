from django.db import models

class Server(models.Model):
	name = models.CharField(max_length=50, verbose_name='Server name', blank=False, null=False)
	ip = models.CharField(max_length=50, verbose_name='IP adress', blank=False, null=False)

	def __str__(self):
		return 'Server: '+self.name