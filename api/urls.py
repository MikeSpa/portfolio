from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.get_projects),
    path("add/", views.add_project, name="add_project"),
    path("update/<int:id>/", views.update_project, name="update_project"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
