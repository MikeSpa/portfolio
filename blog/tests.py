from django.test import TestCase
from .models import Post


class ModelTesting(TestCase):
    def setUp(self):
        self.blog = Post.objects.create(
            title="Setting up a django post for testing",
            author="moi",
            slug="Setting-up-post",
            content="sdakfh askdhfasdhf éadhsf ashdfjasdhfhasdf7a6sdf8 adsf98a7dsf 7as8df .df sd ",
        )

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))

    def test_str(self):
        d = self.blog
        self.assertEqual(str(d), "Setting up a django post for testing")


class ViewTesting(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")
