from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# from django.template import loader
# from django.http import Http404
from .models import Todo

# Create your views here.


def index(request):
    todo_list = Todo.objects.all()
    print('debug', todo_list)
    # context = {
    #     'todo_list': todo_list,
    # }
    return render(request, 'todo/index.html', todo_list)


def add(request):
    if request.method == 'POST':
        task = request.POST.get('task', '')
        Todo.objects.create(task=task)
    return HttpResponseRedirect('index')


# def detail(request, question_id):
#     # return HttpResponse("You'are looking at question {}".format(question_id))
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exist')
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


