from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from .serializers import *
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from .models import Party
from main.open_api.responses import SuccessResponse, SuccessDataResponse

# Create your views here.


class PartyBasicView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                "size",
                OpenApiTypes.INT,
                OpenApiParameter.QUERY,
                description="반환할 개수",
            ),
            OpenApiParameter(
                "page",
                OpenApiTypes.INT,
                OpenApiParameter.QUERY,
                description="반환할 페이지 번호",
            ),
        ],
        responses={200: SuccessDataResponse(data=PartyListSerializer(many=True))},
        tags=["Party"],
        summary="Get party list",
        description="Header에 Authorization: Bearer {token}을 넣어주세요",
    )
    def get(self, request):
        qs = Party.objects.all()
        serializer = PartyListSerializer(qs, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=PartyCreateSerializer,
        responses=SuccessResponse,
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


class PartyDetailView(APIView):
    def get(self, request, col):
        try:
            object = Party.objects.get(col=col)
            return Response(
                col=object.col,
                party_name=object.party_name,
            )

        except:
            raise exceptions.NotFound("Party not found")
