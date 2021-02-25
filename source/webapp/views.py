from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task

def index_view (request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)

def task_view(request):
    if request.method == 'GET':
        task_id = request.GET.get('pk')
        task = Task.objects.get(pk=task_id)
        context = {'task': task}
        task.status = task.status.replace('_', ' ')
        return render(request, 'task_view.html', context)
    elif request.method == 'POST':
        task_id = request.GET.get('pk')
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return redirect('/')

def task_add_view(request):
    if request.method == 'GET':
        return render(request, 'task_add_view.html')
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        completion_date = request.POST.get('completion_date')
        task = Task.objects.create(description=description, status=status, completion_date=completion_date)
        context = {
            'task': task
        }
    return render(request, 'task_view.html', context)

