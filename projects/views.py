from projects.models import Project

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class ProjectList(ListView):
    model = Project
    context_object_name = "projects"


class ProjectDetail(DetailView):
    model = Project
