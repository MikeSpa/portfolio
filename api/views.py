from rest_framework.response import Response
from rest_framework.decorators import api_view

# from django.http import JsonResponse
from projects.models import Project
from .serializers import ProjectSerializer
from rest_framework import status


@api_view(["GET"])
def get_projects(request, format=None):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def add_project(request, format=None):
    if request.method == "GET":
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def update_project(request, id, format=None):
    try:
        project = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
