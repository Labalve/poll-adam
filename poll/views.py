from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from .models import QuestionSet, Question, Answer, Choice


def index(request):
    context = {
        'welcome_message': "Henlo to my website",
        'first_question_id': QuestionSet.objects.get(name="aktywny").question_set.first().id
    }
    return render(request, 'index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def answer(request, question_id, person_id):
    question = get_object_or_404(Question, pk=question_id)
    next_question = question.get_next_question()
    if question.open_question:
        Answer.create_open(person_id, request.POST['answer'], question)
    else:
        choice = get_object_or_404(Choice, pk=request.POST['choice'])
        Answer.create_closed(person_id, choice, question)
    if next_question.id == question_id:
        return HttpResponseRedirect(reverse('finish', args=()))
    return HttpResponseRedirect(reverse('detail', args=(next_question.id,)))


def finish(request):
    context = {
        'thank_you_message': "Dżemkuje za udział :ppppp"
    }
    return render(request, 'finish.html', context)
