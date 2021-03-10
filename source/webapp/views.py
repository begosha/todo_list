from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task
from django.urls import reverse
from webapp.forms import TaskForm

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

def task_add_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_add_view.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)  
        if form.is_valid():  
            task = Task.objects.create(
                description=form.cleaned_data.get('description'),
                details=form.cleaned_data.get('details'),
                status=form.cleaned_data.get('status'),
                completion_date=form.cleaned_data.get('completion_date')
            )
            return redirect('task', pk=task.id)  
        return render(request, 'task_add_view.html', context={'form': form}) 

        # description = request.POST.get('description')
        # details = request.POST.get('details')
        # status = request.POST.get('status')
        # completion_date = request.POST.get('completion_date')
        # task = Task.objects.create(description=description, details=details, status=status, completion_date=completion_date)
        # context = {
        #     'task': task
        # }
        # url = reverse('task', kwargs={'pk': task.pk})
        # return redirect(url)

def guest_add_view(request):
    if request.method == "GET": 
        form = GuestForm()
        return render(request, 'guest_add_view.html', context={'form': form})
    elif request.method == "POST": 
        form = GuestForm(data=request.POST)  
        if form.is_valid():  
            guest = Guest.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                booking_details=form.cleaned_data.get('booking_details')
            )
            return redirect('guest', pk=guest.id)  
        return render(request, 'guest_add_view.html', context={'form': form}) 



