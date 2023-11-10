from django.test import TestCase
from .forms import ContactForm


class FormTesting(TestCase):
    def setUp(self):
        form_data = {
            "name": "Adam",
            "email_address": "a@gmail.com",
            "subject": "Test",
            "message": "Test.",
        }
        self.form = ContactForm(data=form_data)

    def test_form_is_valid(self):
        self.assertTrue(self.form.is_valid())

    def test_contact_form_field_label(self):
        self.assertTrue(
            self.form.fields["name"].label is None
            or self.form.fields["name"].label == "name"
        )
        self.assertTrue(
            self.form.fields["email_address"].label is None
            or self.form.fields["email_address"].label == "email_address"
        )
        self.assertTrue(
            self.form.fields["subject"].label is None
            or self.form.fields["subject"].label == "subject"
        )
        self.assertTrue(
            self.form.fields["message"].label is None
            or self.form.fields["message"].label == "message"
        )


class ViewTesting(TestCase):
    def setUp(self):
        form_data = {
            "name": "Adam",
            "email_address": "a@gmail.com",
            "subject": "Test",
            "message": "Test.",
        }
        self.form = ContactForm(data=form_data)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_view_project_index_uses_correct_template(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")

    def test_view_post_form(self):
        form_data = {
            "name": "Adam",
            "email_address": "a@gmail.com",
            "subject": "Test",
            "message": "Test.",
        }
        response = self.client.post("/contact/", form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/contact/success/")

    def test_view_post_form_with_no_subject_doesnt_send(self):
        form_data = {
            "name": "Adam",
            "email_address": "a@gmail.com",
            "subject": "",
            "message": "Test.",
        }
        response = self.client.post("/contact/", form_data)
        self.assertNotEqual(response.status_code, 302)

    def test_view_post_form_with_no_message_doesnt_send(self):
        form_data = {
            "name": "Adam",
            "email_address": "a@gmail.com",
            "subject": "Test",
            "message": "",
        }
        response = self.client.post("/contact/", form_data)
        self.assertNotEqual(response.status_code, 302)

    def test_view_post_form_and_redirection(self):
        form_data = {
            "name": "Adam",
            "email_address": "a@gmail.com",
            "subject": "Test",
            "message": "Test.",
        }
        response = self.client.get("/contact/", form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/contact/success/")
        self.assertContains(
            response, "Success! Thank you for your message.", status_code=200
        )
