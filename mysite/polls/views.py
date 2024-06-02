from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice, Survey
from .forms import SurveyForm


# Create your views here.

# return HttpResponse("Polls's index#")
    # return HttpResponseRedirect('1')

    # return HttpResponseRedirect(reverse('detail', args=[12]))
    # urls에서 해당 함수에 해당하는 view에 오면 reverse 함수를 통해 다시 detail에 해당하는 urls로 args를 함께 리다이렉트 시킴
def index(request):
    test_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'test_question_list': test_question_list}

    return render(request, 'polls/index.html', context=context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])    # input의 name이 choice = request.POST['choice']
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST) # POST를 받은 data를 SurveyForm에 넣는다
        if form.is_valid():     # validate를 만족할때 True
            # print(form.cleaned_data['user_name'])
            # print(form.cleaned_data['user_age'])

            # update
            # survey = Survey.objects.get(pk=1)
            # form = SurveyForm(request.POST, instance=survey)

            form.save()
            return HttpResponseRedirect(reverse('polls:thanks'))
    else:
        form = SurveyForm()

    return render(request, 'polls/survey_custom.html', {'form': form})

def thanks(request):
    return render(request, 'polls/thanks.html', {})