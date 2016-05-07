from django.shortcuts import render
from rest_framework import generics,permissions
from .models import JGLB
from .serializers import JGLBSerializer 
# Create your views here.

class JGLBList(generics.ListAPIView):
  queryset = JGLB.objects.all()
  serializer_class = JGLBSerializer


class JGLBDetail(generics.RetrieveAPIView):
  queryset = JGLB.objects.all()
  serializer_class = JGLBSerializer

