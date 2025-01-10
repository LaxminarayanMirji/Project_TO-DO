from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import TodoForm
from .models import Todo

# Create your views here.
def home_view(requests):
    # Handle form submission to add new Todo
    form = TodoForm(requests.POST or None)  # To add todo list
    if form.is_valid():
        form.save()
        form = TodoForm()  # Clear the form after saving

    obj = Todo.objects.all()  # Fetch all Todo objects

    context = {"context_form": form, "context_obj": obj}
    return render(requests, "home.html", context)

def delete_view(requests, todo_id):
    # Fetch Todo object or return 404 if not found
    obj = get_object_or_404(Todo, id=todo_id)

    # Handle form submission to delete Todo
    if requests.method == "POST":
        obj.delete()  # Delete the Todo object
        return HttpResponseRedirect("/")  # Redirect back to the homepage

    context = {"context_obj": obj}  # Pass the Todo object to the template
    return render(requests, "delete.html", context)
