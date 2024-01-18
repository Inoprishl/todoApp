from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import TodoModel
from .forms import CreateTaskModelForm
from django.http import Http404, JsonResponse
import re

# Create your views here.
    
def index_view(request):
    form = CreateTaskModelForm()
    context = {'form':form}
    return render(request, 'tasks/index.html', context)

def form_save_view(request):
    if request.method == 'POST':
        form = CreateTaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks'))
    return redirect('/')

def task_edit_view(request, pk):
    buffer_task = get_object_or_404(TodoModel, id=request.GET.get('buffer')) if request.GET.get('buffer') else False
    if buffer_task: buffer_task.delete()
    task = get_object_or_404(TodoModel, id=pk)
    form = CreateTaskModelForm(initial={"title": task.title,'description': task.description, 'status': task.status})
    context = {'form': form, 'pk': pk}
    return render(request, 'tasks/edit.html', context)

def submit_edit_view(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(TodoModel, id=pk)
        raw_form = CreateTaskModelForm(request.POST)
        if raw_form.is_valid():
            form = raw_form.cleaned_data
            buffer_task = TodoModel()
            buffer_task.title = form['title']
            buffer_task.description = form['description']
            buffer_task.status = form['status']
            buffer_task.save()
            return render(request,'tasks/submit_edit.html', context={'b_task': buffer_task, 'task': task})
    return redirect(reverse('tasks'))

def submit_delete_view(request, *args, **kwargs):
    if request.GET.get('pk'):
        pk = request.GET.get('pk')
        if re.fullmatch(r'\d+', pk):
            task = [get_object_or_404(TodoModel, id=pk)]
            is_single=True
        elif pk == 'done':
            task = TodoModel.objects.filter(status=True)
            is_single=False
        else: raise Http404
        return render(request, 'tasks/submit_delete.html', {'tasks': task, 'single': is_single})
    return redirect(reverse('tasks'))

def delete_view(request, *args, **kwargs):
    if request.GET.get('pk'):
        pk = request.GET.get('pk')
        if re.fullmatch(r'\d+', pk):
            task = get_object_or_404(TodoModel, id=pk)
            task.delete()
        elif pk == 'done':
            tasks = TodoModel.objects.filter(status=True)
            tasks.delete()
    return redirect(reverse('tasks'))

def status_change_view(request, pk):
    task = get_object_or_404(TodoModel, id=pk)
    task.status = not task.status
    task.save()
    return redirect(reverse('tasks'))

def submit_delete_done_tasks_view(request):
    tasks = TodoModel.objects.filter(status=True)
    if tasks:
        return render(request, 'tasks/submit_delete_done.html', context={'tasks': tasks})
    return redirect(reverse('tasks'))

def edit_view(request):
    buffer_task = get_object_or_404(TodoModel, id=request.GET.get('buffer')) if request.GET.get('buffer') else False
    task = get_object_or_404(TodoModel, id=request.GET.get('pk')) if request.GET.get('pk') else False
    if buffer_task and task:    
        task.title = buffer_task.title
        task.description = buffer_task.description
        task.status = buffer_task.status
        buffer_task.delete()
        task.save()
    return redirect(reverse('tasks'))

def index_json_view(request):
    todos = TodoModel.objects.all().values()
    return JsonResponse({'todos': list(todos)}, safe=False)

def json_frontend_view(request):
    return render(request, 'json_simple.html')