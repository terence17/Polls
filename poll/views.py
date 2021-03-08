from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .models import Question
# from .models import Choice

# Create your views here.
def index(request):
    return render(request, "poll/index.html")

def detail(request):
    # return HttpResponse("You're looking at question %s." % question_id)

    context = {
        "question" : Question.objects.all()
        # "choice" : Choice.objects.all()
    }

    return render(request, "poll/detail.html", context)
   



def results(request):
    
    return render(request, "poll/results.html")

# def vote(request,):
#     # return HttpResponse("You're voting on question %s." % question_id)  
#     return render(request, "poll/vote.html")  