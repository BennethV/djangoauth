from django.db import models
from staffs.models import Author

# Create your models here.

class Book(models.Model):
	author = models.ForeignKey(Author, on_delete = models.CASCADE)
	name = models.CharField(max_length=120, null=True, blank=True)

	class Meta:
		verbose_name = "Book"
		verbose_name_plural = "Books"

	def __str__(self):
		return self.name
    