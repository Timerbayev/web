from django.contrib import admin
from .models import Question, Answer, Session


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "added_at", "rating", "author"]
    # inlines = (FieldMappingInline)
    # fields = []
    # exclude = ["type"]
    # search_fields = ['category', subCategory','suggestKeyword']
    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ["added_at", "author"]
    # inlines = (FieldMappingInline)
    # fields = []
    # exclude = ["type"]
    # search_fields = ['category', subCategory','suggestKeyword']

    class Meta:
        model = Answer


admin.site.register(Answer, AnswerAdmin)


class SessionAdmin(admin.ModelAdmin):
    list_display = ["user", "key"]

    class Meta:
        model = Answer


admin.site.register(Session, SessionAdmin)

# Register your models here.
