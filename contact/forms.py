from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    subject = forms.CharField(required=True)
    message = forms.CharField(
        widget=forms.Textarea,
        max_length=2000,
        # help_text="Enter your message",
        required=True,
    )
