from django.shortcuts import render, get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MoviesSerializer

class Movies(APIView):
    def get_object(self, pk):
        obj = get_object_or_404(Movies, pk=pk)
        return obj

    def get(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = MoviesSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = MoviesSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

