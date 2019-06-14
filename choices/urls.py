from django.urls import path
from . import views

app_name = 'choices'

urlpatterns = [
    path('<int:question_pk>/answer_delete/<int:answer_pk>/', views.answer_delete, name="answer_delete"),
    path('<int:question_pk>/question_delete/', views.question_delete, name="question_delete"),
    path('new/', views.new, name="new"),
    path('<int:question_pk>/vote/', views.vote, name="vote"),
    path('', views.index, name="index"),
]