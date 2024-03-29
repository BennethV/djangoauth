from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=120, null=True, blank=True)

	class Meta:
		verbose_name = "Author"
		verbose_name_plural = "Authors"

	def __str__(self):
		return self.name
    