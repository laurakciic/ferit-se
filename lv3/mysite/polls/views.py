from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed
from .models import Question
from django.template import loader
from django.shortcuts import render

def test(request):
    txt = "<h1>Test</h1>"
    questions = Question.objects.all()
    for q in questions:
        qtxt = str(q) 
        txt = txt + qtxt + "</br>"

    return HttpResponse(txt)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def welcome(request):
    return HttpResponse("<h1>Welcome!</h1>")

def kovacic(request):
    return HttpResponse("<h1>kovacic</h1>")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)