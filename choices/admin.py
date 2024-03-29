from django.contrib import admin
from .models import Question, Answer

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=("title", "selection1", "selection2")
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display=("pick", "comment")
admin.site.register(Answer, AnswerAdmin)