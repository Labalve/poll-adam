from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import random
import string
from django.template import loader
from .models import QuestionSet, Question, Answer, Choice


def index(request):
    person_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(1, 21)])
    context = {
        'welcome_message': "Henlo to my website",
        'first_question_id': QuestionSet.objects.get(name="aktywny").question_set.first().id,
        'person_id': person_id
    }
    return render(request, 'index.html', context)


def detail(request, question_id, person_id=False):
    question = get_object_or_404(Question, pk=question_id)
    if not person_id:
        random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(1, 21)])
        question = get_object_or_404(Question, pk=question_id)
        person_id = random
    context = {
        'question': question,
        'person_id': person_id
    }
    return render(request, 'detail.html', context)


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
    return HttpResponseRedirect(reverse('detail', args=(next_question.id, person_id,)))


def finish(request):
    context = {
        'thank_you_message': "Dżemkuje za udział :ppppp"
    }
    return render(request, 'finish.html', context)
