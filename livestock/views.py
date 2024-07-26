from .models import LiveStock, Farm
from rest_framework import generics
from .serializers import LivestockSerializer, FarmSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CreateLivestockView(generics.CreateAPIView):
    queryset = LiveStock.objects.all
    serializer_class = LivestockSerializer
    permission_classes = [AllowAny]

class RetrieveUpdateDeleteLivestockView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LiveStock.objects.all()
    serializer_class = LivestockSerializer
    permission_classes = [IsAuthenticated]

   