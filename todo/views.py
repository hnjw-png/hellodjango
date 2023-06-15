from django.shortcuts import render

# Create your views here.

def get_todo_list(request):
    return render(request, '/workspace/hellodjango/todo/templates/todo2/todo_list.html')
