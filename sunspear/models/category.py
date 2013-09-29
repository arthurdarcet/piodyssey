from django.db import models
from django.contrib import admin
from django.contrib.auth.models import Group


class Category(models.Model):
    class Meta:
        app_label = 'sunspear'
        verbose_name_plural = 'categories'
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.title


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)
