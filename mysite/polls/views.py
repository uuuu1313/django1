from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

# return HttpResponse("Polls's index#")
    # return HttpResponseRedirect('1')

    # return HttpResponseRedirect(reverse('detail', args=[12]))
    # urls에서 해당 함수에 해당하는 view에 오면 reverse 함수를 통해 다시 detail에 해당하는 urls로 args를 함께 리다이렉트 시킴
def index(request):
    ctx = {
        "greetings": "Hellow there!",
        "location": {
            "city": "Seoul",
            "county": "South Korea"
        },
        "languages": ["Korean", "English"]
    }

    return render(request, 'polls/main.html', context=ctx)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)