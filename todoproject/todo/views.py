from django.shortcuts import render, redirect
from todo.models import Todo
from todo.forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})



def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # Redirect to the list view after saving
    else:
        form = TodoForm()
    
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_delete_confirm.html', {'todo': todo})
