# from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def contactView(request):
    # GET
    if request.method == "GET":
        form = ContactForm()
    # POST
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            body = {
                "name": "Name: " + form.cleaned_data["name"],
                "email_address": "Email: " + form.cleaned_data["email_address"],
                "subject": "Subject: " + form.cleaned_data["subject"],
                "message": "Message: " + form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            try:
                send_mail(
                    subject, message, name, ["admin@example.com"]
                )  # subject, message, name, [to]
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "contact/contact.html", {"form": form})


def successView(request):
    return HttpResponse("Success! Thank you for your message.")
