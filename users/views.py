from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import UserSerializer
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def patch(self, request, *args, **kwargs):
        response = super().patch(request, *args, **kwargs)
        print("Response data:", response.data)
        return response


class UserRegistration(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
