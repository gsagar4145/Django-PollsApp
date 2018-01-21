from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from django.urls import reverse

from .models import Question,Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'pollsApp/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'pollsApp/detail.html',{'question':question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
	question = get_object_or_404(Question,pk=question_id)