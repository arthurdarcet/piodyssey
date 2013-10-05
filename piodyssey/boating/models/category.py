from django.db import models


class Category(models.Model):
    class Meta:
        app_label = 'boating'
        verbose_name_plural = 'categories'
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.title

