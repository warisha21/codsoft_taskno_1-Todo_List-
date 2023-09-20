from django.shortcuts import render
from django.http import HttpResponse
from home.models import Tasks

# Create your views here.
def home(request):
    context = {'success' : False , 'name' : 'warisha'}
    if request.method == "POST":
        # when submit the form
        tittle= request.POST['tittle']
        desc = request.POST['desc']
        print(tittle, desc)

        ins = Tasks(taskTittle = tittle, taskDescription= desc)
        ins.save()
        context = {'success' : True}

    # if form not submit
    return render (request, 'index.html', context)

def tasks(request):
    allTasks = Tasks.objects.all()
    # print(allTasks)
    # for items in allTasks:
    #     print(items.taskTittle)
    #     print(items.taskDescription)

    context = {'tasks' : allTasks}
    return render (request, 'tasks.html', context)
