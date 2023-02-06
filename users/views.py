from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, Token
from .models import User
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from main.open_api.responses import *

# Create your views here.


class Register(APIView):
    permission_classes = []

    @extend_schema(
        request=UserSerializer,
        responses={200: SuccessSimpleResponse},
        tags=["User"],
        summary="Register",
        description="",
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("success")
        return Response("register")


class Login(APIView):
    permission_classes = []

    @extend_schema(
        request=UserSerializer,
        responses={200: SuccessSingleDataResponse(data=UserTokenResponseSerializer())},
        tags=["User"],
        summary="Register",
        description="",
    )
    def post(self, request):
        # print(request.data["email"], request.data["password"])
        user = User.authenticate(email=request.data["email"], password=request.data["password"])
        if user is not None and user is not False:
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            return Response(
                {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                }
            )
        else:
            raise AuthenticationFailed("Invalid credentials")


class Refresh(APIView):
    permission_classes = []

    @extend_schema(
        request=UserSerializer,
        responses={200: SuccessSingleDataResponse(data=UserTokenResponseSerializer())},
        tags=["User"],
        summary="Register",
        description="",
    )
    def post(self, request):
        refresh_token = request.data["refresh_token"]

        refresh = RefreshToken(refresh_token)
        refresh.verify()

        print(refresh.payload.get("user_id"))
        print(refresh.access_token)

        return Response(
            {
                "access_token": str(refresh.access_token),
            }
        )
