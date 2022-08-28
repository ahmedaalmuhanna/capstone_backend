from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import CreateUserSerializer, LoginUserSerializer

# Create your views here.


class CreateUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    
    
class LoginUserAPIView(APIView):
    serializer_class = LoginUserSerializer
    
    def post(self, request):
        my_data = request.data
        serializer = LoginUserSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)