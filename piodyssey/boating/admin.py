from django.contrib import admin

from .models import Answer, Category, Question, Session


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('slug', 'question', 'category', 'scraper')
    list_filter = ('category', 'scraper')
    search_fields = ('question', '_responseA', '_responseB', '_responseC', '_responseD')
    ordering = ('scraper', 'category', 'slug')
admin.site.register(Question, QuestionAdmin)


class AnswerAdminInline(admin.StackedInline):
    model = Answer
    template = 'admin/inline-answers.html'
    extra = 0


class SessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'created_at')
    inlines = (AnswerAdminInline, )


admin.site.register(Session, SessionAdmin)
