# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework import generics,permissions
from .models import JGLB,SFXZJGJBXX
from .serializers import JGLBSerializer,SFXZJGJBXXSerializer 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
# Create your views here.

# serializer for JGLB 机构类别
class JGLBList(generics.ListAPIView):
  queryset = JGLB.objects.all()
  serializer_class = JGLBSerializer

class JGLBDetail(generics.RetrieveAPIView):
  queryset = JGLB.objects.all()
  serializer_class = JGLBSerializer

# serializer for SFXZJGJBXX 司法行政机关基本信息
class SFXZJGJBXXList(APIView):

  def get(self,request,format=None):
    sfxzjgjbxxs = SFXZJGJBXX.objects.all()
    serializer = SFXZJGJBXXSerializer(sfxzjgjbxxs,many=True)
    return Response(serializer.data)

  def post(self,request,format=None):
    serializer = SFXZJGJBXXSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)



class SFXZJGJBXXDetail(APIView):

  def get_object(self,pk):
    try:
      return SFXZJGJBXX.objects.get(pk=pk)
    except SFXZJGJBXX.DoesNotExist:
      raise Http404

  def get(self,request,pk,format=None):
    sfxzjgjbxx = self.get_object(pk)
    serializer = SFXZJGJBXXSerializer(sfxzjgjbxx)
    return Response(serializer.data)

  def put(self,request,pk,format=None):
    sfxzjgjbxx = self.get_object(pk)
    serializer = SFXZJGJBXXSerializer(sfxzjgjbxx,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk,format=None):
    sfxzjgjbxx = self.get_object(pk)
    sfxzjgjbxx.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



