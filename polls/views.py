from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Question,Choice
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.template import loader
# Create your views here.

def parent(request):

    return render(request,'polls/parent.html')

def child(request):
    return render(request,'polls/child.html')

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')
    context ={
        'latest_question_list':latest_questions,
    }
    return render(request,'polls/index.html',context)

def error(request):
    # q=Question(question_text='hello world',pub_date='')
    # q.choice_set
    raise Http404('wrong!')

def detail(request,question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    #     context ={'question':question}
    # except:
    #     raise Http404('That question does not exist')
    # return render(request,'polls/detail.html',context)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error_message':'Did not select a choice'})

    selected_choice.votes+=1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/resul' \
                    'ts.html'
