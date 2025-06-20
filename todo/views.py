from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

@api_view(["GET", "POST"])
def task_list_create(request):
    if request.method == "GET":
        tasks = Task.objects.all().order_by("-created")
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)
    
    
@api_view(["GET",'PUT','DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        Response({"error":"Task not found"})
        
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "DELETE":
        task.delete()
        return Response()