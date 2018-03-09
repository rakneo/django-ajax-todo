from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from .models import Todo

import json
# Create your views here.


def homepage(request):

    todo_uc_count = Todo.objects.filter(is_completed=False).count()
    todo_uc = Todo.objects.filter(is_completed=False)
    todo_c = Todo.objects.filter(is_completed=True)
    context = {
        "todo_uc_count":todo_uc_count,
        "todos_uc": todo_uc,
        "todos_c":  todo_c
    }
    return render(request, "index.html", context)


def update_event_completed(request, pk):

    data = dict()
    print("func called")
    todo = Todo.objects.filter(pk=pk)

    if request.method == 'GET':

        todo.update(is_completed=True)

        todo_c = Todo.objects.filter(is_completed=True)
        todo_uc = Todo.objects.filter(is_completed=False)
        data['is_form_valid'] = True
        data['result'] = "event successfully updated"
        data['html_data1'] = render_to_string(
            'partial_list/done-items.html', {
                'todos_c': todo_c
            }
        )
        data['html_data2'] = render_to_string(
            'partial_list/not-done-items.html', {
                'todos_uc': todo_uc
            }
        )
        return HttpResponse(
            json.dumps(data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def event_delete(request, pk):

    data = dict()
    print("func called")
    todo = Todo.objects.filter(pk=pk)

    if request.method == 'GET':

        todo.delete()

        todo_c = Todo.objects.filter(is_completed=True)
        data['is_form_valid'] = True
        data['result'] = "event successfully deleted"
        data['html_data'] = render_to_string(
            'partial_list/done-items.html', {
                'todos_c': todo_c
            }
        )

        return HttpResponse(
            json.dumps(data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def add_event(request):

    data = dict()

    if request.method == 'POST':
        todo_event = request.POST.get('todo_event')
        new_todo = Todo(event=todo_event)
        new_todo.save()

        todo_uc = Todo.objects.filter(is_completed=False)
        data['is_form_valid'] = True
        data['result'] = "Event Added Successfully!"
        data['html_data'] = render_to_string(
            'partial_list/not-done-items.html', {
                'todos_uc': todo_uc
            })
        return HttpResponse(
            json.dumps(data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )






