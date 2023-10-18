from django.http import HttpResponse
from .models import Question
from django.shortcuts import render

def index(request):
    questions=Question.objects.all()
    context={"questions":questions}
    return render(request,"polls/index.html",context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s"% question_id)

def results(request,question_id):
    response="You're looking at the results of questions %s."
    return HttpResponse(response %question_id)

def vote (request, question_id):
    return HttpResponse("You're voting on question %s.")

