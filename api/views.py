from rest_framework.response import Response
from rest_framework.decorators import api_view
from projects.models import Project
from .serializers import ProjectSerializer


@api_view(["GET"])
def getData(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addProject(request):
    serializer = ProjectSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    print(serializer.errors)
    return Response(serializer.data)
