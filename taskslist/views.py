from django.shortcuts import render
from django.views.generic import TemplateView

class TasksView(TemplateView):
    template_name = 'taskslist/tasks.html'
