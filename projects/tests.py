from django.test import TestCase
from .models import Project


class ModelTesting(TestCase):
    def setUp(self):
        self.blog = Project.objects.create(
            title="Setting up a project for testing",
            author="moi",
            slug="Setting-up-project",
            description="sakfhésdhféakhfd",
            url="",
            image="",
        )

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Project))

    def test_str(self):
        d = self.blog
        self.assertEqual(str(d), "Setting up a project for testing")


class ViewTesting(TestCase):
    def setUp(self):
        self.blog = Project.objects.create(
            title="Setting up a project for testing",
            author="moi",
            slug="Setting-up-project",
            description="sakfhésdhféakhfd",
            url="",
            image="",
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)

    def test_view_project_list_uses_correct_template(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects/project_list.html")

    def test_view_project_detail_uses_correct_template(self):
        response = self.client.get("/projects/1/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects/project_detail.html")
