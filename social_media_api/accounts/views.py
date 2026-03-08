from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)

            return Response({
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "token": token.key
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "username": user.username,
            "email": user.email,
            "bio": user.bio
        })
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):

    try:
        user_to_follow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    request.user.following.add(user_to_follow)

    return Response({"message": f"You are now following {user_to_follow.username}"})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):

    try:
        user_to_unfollow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    request.user.following.remove(user_to_unfollow)

    return Response({"message": f"You unfollowed {user_to_unfollow.username}"})
