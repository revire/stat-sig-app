from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user

from django.urls import reverse

from polls.forms import NameForm, UploadFileForm

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
#from django.urls import reverse

from django.views.generic import TemplateView

from django.contrib.auth.models import User

from .models import Choice, Question, Data

class IndexView(TemplateView):
    template_name = 'polls/home.html'


    def get(self, request):
        words = list(Data.objects.all())[-5:]
        words.reverse()
        form = NameForm()
        return render(request, self.template_name, {'form': form, 'words': words})

    def post(self, request):
        form = NameForm(request.POST)
        words = list(Data.objects.all())[-5:]
        words.reverse()
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            text = form.cleaned_data['post']
            l = len(text)
            form = NameForm()

        context = {'form' : form, 'text': text, 'len': l, 'words': words}
        return render(request, self.template_name, context)

from .analyze.analyze import analyze

class AnalyzeView(TemplateView):
    template_name = 'polls/analyze.html'

    def get(self, request):

        fileform = UploadFileForm()
        context = {'form':fileform}
        return render(request, self.template_name, context)

    def post(self, request):

        file = UploadFileForm(request.POST, request.FILES)
        print(type(file))
        if file.is_valid():
            path = request.FILES['file']
            print(path)
            # file is saved
            l  = analyze(path)
            file.save()
            print(l)
            # l = 2
            fileform = UploadFileForm()

        context = {'form':fileform, 'file':file, 'len':l}
        return render(request, self.template_name, context)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




