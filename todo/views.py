from django.shortcuts import render
from .models import Item

# Create your views here.

def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, '/workspace/hellodjango/todo/templates/todo2/todo_list.html', context)
    
def add_item(request):
    return render(request, 'todo/templates/todo2/add_item.html')
