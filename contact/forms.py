from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    subject = forms.CharField(max_length=50, required=True)
    message = forms.CharField(
        widget=forms.Textarea,
        max_length=2000,
        # help_text="Enter your message",
        required=True,
    )

    class Meta:
        model = Contact
        fields = ("name", "email_address", "subject", "message")
