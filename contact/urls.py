from django.urls import path

from . import views
from .views import ContactView

urlpatterns = [
    # path("", views.contact_view, name="contact"),
    path("", ContactView.as_view(), name="contact"),
    path("success/", views.success_view, name="success"),
]
