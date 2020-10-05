from django.shortcuts import render
from rest_framework import generics
from descriptions.serializers import CreateDescriptionSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CreateDescriptionView(generics.CreateAPIView):
    serializer_class = CreateDescriptionSerializer
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated,]

create_description = CreateDescriptionView.as_view()