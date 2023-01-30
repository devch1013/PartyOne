from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from drf_spectacular.utils import extend_schema
from .models import Party

# Create your views here.


class PartyBasicView(APIView):
    @extend_schema(
        responses={200: PartyListSerializer(many=True)},
        tags=["Party"],
        summary="Create new party",
        description="Header에 Authorization: Bearer {token}을 넣어주세요",
    )
    def get(self, request):
        qs = Party.objects.all()
        serializer = PartyListSerializer(qs, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=PartyCreateSerializer,
        responses={200: PartyCreateSerializer},
        tags=["Party"],
        summary="Create new party",
        description="Header에 Authorization: Bearer {token}을 넣어주세요",
    )
    def post(self, request):
        serializer = PartyCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(host=request.user)
            return Response("success")
        return Response("PartyBasicView")
