from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import UserLoginSerializer, UserSerializer
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import get_user_model

User = get_user_model()



class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Ensure this view requires authentication


class UserDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def patch(self, request, *args, **kwargs):
        response = super().patch(request, *args, **kwargs)
        print("Response data:", response.data)
        return response


class UserRegistration(generics.CreateAPIView):
    permission_classes = [AllowAny]  # Allow unauthenticated access to login view

    serializer_class = RegistrationSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated access to login view

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user_data = UserSerializer(user).data
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': user_data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)