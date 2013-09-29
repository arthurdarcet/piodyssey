from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Category, Question


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class QuestionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Question, QuestionAdmin)

admin.site.unregister(Group)
