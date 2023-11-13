from django.http import HttpResponse
from .forms import ContactForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class ContactView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    success_url = reverse_lazy("success")
    template_name = "contact/contact.html"

    def form_invalid(self, form):
        return HttpResponse("Invalid header found.")


def success_view(request):
    return HttpResponse("Success! Thank you for your message.")
