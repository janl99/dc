# models serializer 

from rest_framework import serializers
from .models import JGLB


class JGLBSerializer(serializers.ModelSerializer):
  #parent = serializers.Field(source='parent.text')

  class Meta:
    model = JGLB
    fields = ('id','code','text','note','parent')
