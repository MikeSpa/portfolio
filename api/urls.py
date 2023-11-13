from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.ProjectList.as_view(), name="view_projects"),
    path("update/<int:pk>/", views.ProjectDetail.as_view(), name="update_project"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
