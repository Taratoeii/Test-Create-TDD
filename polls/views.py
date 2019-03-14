from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.shortcuts import HttpResponse
from .models import Choice, Question
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

def index(request):
    template = loader.get_template('text.html')
    context = {
        'name': "what",
    }
    return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))

def Delete(request):
    question = Question.objects.all()
    try:
        selected_question = Question.objects.get(id=request.POST['question'])
    except (KeyError, Question.DoesNotExist):
        return render(request, 'index.html', {
            'error_message': "You didn't select a question.",
        })
    else:
        selected_question.delete()
    return HttpResponseRedirect(reverse('polls:index'))

def Add(request):
    Question.objects.create(question_text=request.POST['Addtext'], pub_date=timezone.now())
    return HttpResponseRedirect(reverse('polls:index'))