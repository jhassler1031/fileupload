from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from file_app.serializers import FileSerializer
from file_app.models import File

# Create your views here.
class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def get(self, request):
      files = File.objects.all()
      serialized_files = FileSerializer(files, many=True)
      return Response(serialized_files.data, 200)

  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)

    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDestroyView(APIView):
    def delete(self, request, pk):
        file = File.objects.get(id=pk)
        file.delete()
        return Response("", 204)
