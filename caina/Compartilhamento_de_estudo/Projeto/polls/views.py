from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question

def index(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, "polls/index.html", context)
    
def detail(request, question_id):
    question= get_object_or_404 (Question, pk=question_id)
    return render(request,"polls/detail.html",{"question": question})

def results(request, question_id):
    response= get_object_or_404(request)
    return render(request,"polls/results.html", response)

def vote (request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)