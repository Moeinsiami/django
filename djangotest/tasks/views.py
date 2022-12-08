from django.shortcuts import render

tasks = ['check mail', 'send gift', 'shop']
# Create your views here.
def index(request):
    return render(request, 'tasks/index.html',{
        "tasks": tasks
    })