from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import FileListSerializers
from rest_framework.parsers import MultiPartParser

# Create your views here.

def home(request):
    return render(request, 'home.html')

def download(request,uid):
    return render(request,'download.html',context={'uid': uid})

class HandleFileUploadView(APIView):
    
    def post(self, request):
        try:
            data = request.data
            print("Received data:", data)  # Add this line for debugging
            serializer = FileListSerializers(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200, 'messages': 'Files uploaded successfully'})
            return Response({'status': 400, 'messages': 'Something Went Wrong', 'data': serializer.errors})

        except Exception as e:
            print("Exception:", e)  # Add this line for debugging
