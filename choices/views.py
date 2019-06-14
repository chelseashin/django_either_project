from django.shortcuts import render, redirect
from .models import Question, Answer
import requests
import os

# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        selection1 = request.POST.get('selection1')
        selection2 = request.POST.get('selection2')
        question = Question(title=title, selection1=selection1, selection2=selection2)
        question.save()
        return redirect('choices:index')
    else:
        questions = Question.objects.all()
        context = {
            'questions' : questions,
            }
        return render(request, 'choices/index.html', context)
        
def vote(request, question_pk):
    if request.method == "POST":
        print(request.POST.get('pick'))
        pick = int(request.POST.get('pick'))
        
        comment = request.POST.get('comment')
        answer = Answer(pick=pick, comment=comment, question_id=question_pk)
        answer.save()
        return redirect('choices:vote', question_pk=question_pk)
    else:
        question = Question.objects.get(pk=question_pk)
        GIPHY_API = 'b0GIlipiKq6qMKrOdSVxAAKRgjYK1Otn'
        url1 = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API}&q={question.selection1}&limit=1&lang=ko'
        url2 = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API}&q={question.selection2}&limit=1&lang=ko'
        data1 = requests.get(url1).json()
        data2 = requests.get(url2).json()
        image1 = data1.get('data')[0].get('images').get('original').get('url')
        image2 = data2.get('data')[0].get('images').get('original').get('url')
        answers = question.answer_set.all()

        if len(answers) !=0:
            pick1 = question.answer_set.filter(pick=0).count()
            pick1_per = str(round(pick1/len(answers)*100))+'%'
            pick2 = question.answer_set.filter(pick=1).count()
            pick2_per = str(round(pick2/len(answers)*100))+'%'
        else: 
            pick1_per ='0'
            pick2_per ='0'
        
        context = {
            'question' : question,
            'answers' : answers,
            'pick1_per': pick1_per,
            'pick2_per' : pick2_per,
            'image1' : image1,
            'image2' : image2,
            }
        return render(request, 'choices/vote.html', context)
        
def new(request):
    return render(request, 'choices/new.html')
    
def question_delete(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    question.delete()
    return redirect('choices:index')
    
def answer_delete(request, question_pk, answer_pk):
    answer = Answer.objects.get(pk=answer_pk)
    answer.delete()
    return redirect('choices:vote', question_pk)
    

    
