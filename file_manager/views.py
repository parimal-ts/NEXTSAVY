from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import FileManager
from django.contrib import messages
from .serializers import FileSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def file_list(request):
    """
    This function retrieves all files from the FileManager model and renders them in a template called
    "file_list.html".
    
    :param request: The request parameter is an object that represents the HTTP request made by the
    client to the server. It contains information such as the HTTP method used (GET, POST, etc.), the
    URL requested, any data submitted in the request, and more. The view function uses this object to
    generate an appropriate response
    :return: The function `file_list` returns an HTTP response that renders the `file_list.html`
    template with a context dictionary containing all the `FileManager` objects retrieved from the
    database.
    """
    files = FileManager.objects.all()
    return render(request, "file_list.html", {"files": files})

def upload(request):
    """
    This function handles file uploads through a form and saves the file to a database using Django's
    file storage system.
    
    :param request: The request object represents the HTTP request that the server receives from the
    client. It contains information about the request, such as the HTTP method (GET, POST, etc.),
    headers, and any data that was sent with the request
    :return: The view is returning an HTTP response with a JSON object containing a status code, a
    message, and an empty list of data.
    """
    if request.method == 'GET':
        return render(request, "upload.html")
    elif request.method == 'POST' and request.FILES['file']:
        upload = request.FILES['file']

        try:
            file = FileManager.objects.create(file=upload)
            messages.info(request, 'File uploaded successfully!')
        except Exception as e:
            print(e)
        response = {
                "status_code": status.HTTP_200_OK,
                "message":"file uploaded successfully",
                "data" : []
            }
        return JsonResponse(response)


# This is a class that retrieves a list of files using a RetrieveAPIView and a FileSerializer in
# Django.
class GetFileListView(RetrieveAPIView):
    queryset = FileManager.objects.all()
    serializer_class = FileSerializer

    def retrieve(self, request, pk, *args, **kwargs):
        instance = FileManager.objects.filter(id=pk)

        serializer = self.get_serializer(instance, many=True)
        response = {
            "status_code": status.HTTP_200_OK,
            "message":"file retrieve",
            "data" : serializer.data
        }
        if not instance:
            response = {
            "status_code": status.HTTP_404_NOT_FOUND,
            "message":"file not found",
            "data" : None
        }
        return Response(response)



