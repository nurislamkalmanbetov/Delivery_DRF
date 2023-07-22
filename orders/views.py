from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class HelloOrderView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"mesage":"Hello Orders"},status=status.HTTP_200_OK)
