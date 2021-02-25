from django.shortcuts import render
from webapp.models import Task

def index_view (request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)

def task_view(request):
    task_id = request.GET.get('pk')
    task = Task.objects.get(pk=task_id)
    context = {'task': task}
    task.status = task.status.replace('_', ' ')
    print(task.completion_date)
    return render(request, 'task_view.html', context)

def task_add_view(request):
    if request.method == 'GET':
        return render(request, 'task_add_view.html')
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        completion_date = request.POST.get('completion_date')
        print(completion_date)
        task = Task.objects.create(description=description, status=status, completion_date=completion_date)
        context = {
            'task': task
        }
    return render(request, 'task_view.html', context)
