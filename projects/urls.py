from django.urls import path

# from projects import views
from .views import ProjectList, ProjectDetail


urlpatterns = [
    path("", ProjectList.as_view(), name="project_index"),
    path("<int:pk>/", ProjectDetail.as_view(), name="project_detail"),
]
