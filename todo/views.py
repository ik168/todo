from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# from django.template import loader
# from django.http import Http404
from .models import Todo

# Create your views here.


def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'todo/index.html', context)


def add(request):
    if request.method == 'POST':
        task = request.POST.get('task', '')
        Todo.objects.create(task=task)
    return HttpResponseRedirect('/todo/')


def delete(request, todo_id):
    t = get_object_or_404(Todo, pk=todo_id)
    t.delete()
    return HttpResponseRedirect('/todo/')


def edit(request, todo_id):
    t = get_object_or_404(Todo, pk=todo_id)
    context = {
        't': t,
    }
    return render(request, 'todo/edit.html', context)


def update(request, todo_id):
    t = get_object_or_404(Todo, pk=todo_id)
    task = request.POST.get('task', '')
    # print('debug', task, t.task)
    t.task = task
    t.save()
    return HttpResponseRedirect('/todo/')




