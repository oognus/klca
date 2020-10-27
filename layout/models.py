from django.db import models

# Create your models here.
class Home(models.Model):
	title = models.CharField(max_length=35)

	class Meta:
		verbose_name = "Home"
		verbose_name_plural = "Homes"

	def __str__(self):
		return self.title
    