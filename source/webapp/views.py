from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task
from django.urls import reverse

def index_view (request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    url = reverse('index')
    return render(request, 'index.html', context)

def task_view(request, pk):
    if request.method == 'GET':
        task = Task.objects.get(pk=pk)
        context = {'task': task}
        task.status = task.status.replace('_', ' ')
        return render(request, 'task_view.html', context)
    elif request.method == 'POST':
        task_id = request.GET.get('pk')
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')

def task_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'task_add_view.html')
    elif request.method == 'POST':
        description = request.POST.get('description')
        details = request.POST.get('details')
        status = request.POST.get('status')
        completion_date = request.POST.get('completion_date')
        task = Task.objects.create(description=description, details=details, status=status, completion_date=completion_date)
        context = {
            'task': task
        }
        return redirect('task', pk=task.pk)

