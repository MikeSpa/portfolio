from django.test import TestCase, Client
from projects.models import Project
from django.urls import reverse
from rest_framework import status
from .serializers import ProjectSerializer
import json

# from rest_framework.test import APIRequestFactory

client = Client()


class ViewTesting(TestCase):
    def setUp(self):
        """SetUp 3 projects"""
        Project.objects.create(
            title="Project 1",
            author="moi",
            slug="project-1",
            description="sakfhésdhféakhfd",
            url="www.smth.com",
            image="",
        )
        Project.objects.create(
            title="Project 2",
            author="moi",
            slug="project-2",
            description="sakfhésdhféakhfd",
            url="www.smthelse.com",
            image="",
        )
        Project.objects.create(
            title="Project 3",
            author="moi",
            slug="project-3",
            description="sakfhésdhféakhfd",
            url="www.project-3.com",
            image="",
        )

    # TEST for get_project
    def test_get_all_project(self):
        # get API response
        response = client.get("/api/")
        # Serialize data from DB
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_all_project_json(self):
        # get API response
        response = client.get("/api/.json")
        # Serialize data from DB
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # TEST for add_project

    # def test_add_project_get_all_project(self):
    #     # get API response
    #     response = client.get("/api/add/")
    #     # Serialize data from DB
    #     projects = Project.objects.all()
    #     serializer = ProjectSerializer(projects, many=True)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, serializer.data)

    def test_add_valid_project(self):
        valid_project = {
            "title": "Project 4",
            "author": "moi",
            "slug": "project-4",
            "description": "sakfhésdhféakhfd",
            "url": "https://www.something.com",
        }
        # post valid project
        response = client.post(
            reverse("view_projects"),
            data=json.dumps(valid_project),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_project(self):
        invalid_project = {
            "author": "moi",
            "slug": "project-4",
            "description": "sakfhésdhféakhfd",
            "url": "www.smthelse.com",
            "image": "",
        }
        # post invalid project
        response = client.post(
            reverse("view_projects"),
            data=json.dumps(invalid_project),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # TEST for update_project
    # GET
    def test_update_project_get_valid_project(self):
        response = client.get(reverse("update_project", kwargs={"pk": 1}))
        project = Project.objects.get(pk=1)
        serializer = ProjectSerializer(project)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_project_get_invalid_project(self):
        response = client.get(reverse("update_project", kwargs={"pk": 12}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # PUT
    def test_update_project_put_valid_project(self):
        valid_project = {
            "title": "New Project 1",
            "author": "moi",
            "slug": "project-1-new",
            "description": "sakfhésdhféakhfd",
            "url": "https://www.something.com",
        }
        response = client.put(
            reverse("update_project", kwargs={"pk": 1}),
            data=json.dumps(valid_project),
            content_type="application/json",
        )
        project = Project.objects.get(pk=1)
        serializer = ProjectSerializer(project)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_project_put_invalid_project(self):
        invalid_project = {
            "title": "New Project 1",
            "author": "moi",
            "slug": "project-1-new",
            "description": "sakfhésdhféakhfd",
        }
        response = client.put(
            reverse("update_project", kwargs={"pk": 1}),
            data=json.dumps(invalid_project),
            content_type="application/json",
        )
        project = Project.objects.get(pk=1)
        serializer = ProjectSerializer(project)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response.data, serializer.data)

    # DELETE
    def test_update_project_delete(self):
        response = client.delete(reverse("update_project", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_project_delete_not_existant(self):
        response = client.delete(reverse("update_project", kwargs={"pk": 4}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
