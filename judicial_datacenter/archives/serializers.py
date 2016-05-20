# -*- coding: utf-8 -*-
# models serializer 

from rest_framework import serializers
from .models import JGLB,SFXZJGJBXX

# Serializer for JGLB 机构类别
class JGLBSerializer(serializers.ModelSerializer):

  class Meta:
    model = JGLB
    fields = ('id','code','text','note','parent')

# Serializer for SFXZJGJBXX 司法行政机关基本信息
class SFXZJGJBXXSerializer(serializers.ModelSerializer):
  JGLB = serializers.CharField(source='JGLB.code')
  JGXZJB = serializers.CharField(source='JGXZJB.code')
  JGLSCJ = serializers.CharField(source='JGLSCJ.code')
  SJSFXZZGJG = serializers.CharField(source='SJSFXZZGJG.JGBM')
  SJSFXZZGBM = serializers.CharField(source='SJSFXZZGBM.JGBM')

  class Meta:
    model = SFXZJGJBXX
    fields = ('id','JGBM','JGMC','JGJC','YWMC','JGDM','FZR','JGLB','JGXZJB','JGLSCJ','SJSFXZZGJG','SJSFXZZGBM','LXDH','CZHM','DZYX','YB','DZ') 


  def create(self,validated_data):
    # Validate JGLB code is exist,and convert it. it is required.
    jglb_code = validated_data.pop('JGLB')
    jglb = JGLB.objects.get(code=jglb_code['code'])
    if not jglb:
      raise ValidationError({'JGLB','%s dose not exist,it is required.' % jglb_code['code']})
    validated_data['JGLB'] = jglb

    # Validate JGXZJB code is exist, and convert it ,it is not required.
    jgxzjb_code = validated_data.pop('JGXZJB')
    jgxzjb = JGXZJB.objects.get(code=jgxzjb_code['code'])
    if not jgxzjb:
      jgxzjb = None
    validated_data['JGXZJB'] = jgxzjb

    # Validate JGLSCJ code is exist, and convert it.it is required.
    jglscj_code = validated_data.pop('JGLSCJ')
    jglscj = JGLSCJ.objects.get(code=jglscj_code['code'])
    if not jglscj:
      raise ValidationError({'JGLSCJ','%s dose not exist,it is required.' % jglscj_code['code']})
    validated_data['JGLSCJ'] = jglscj

    # Validate SJSFXZZGJG.JGBM is exist, and convert it, it is required when it is no parent .
    sjsfxzzgjg_jgbm = validated_data.pop('SJSFXZZGJG')
    sjsfxzzgjg = SFXZJGJBXX.objects.get(JGBM=sjsfxzzgjg_jgbm['JGBM'])
    if not sjsfxzzgjg:
      sjsfxzzgjg = None
    validated_data['SJSFXZZGJG'] = sjsfxzzgjg

    # Validate SJSFXZZGBM.JGBM is exist, and convert it , it is required where it is no parent.
    sjsfxzzgbm_jgbm = validated_data.pop('SJSFXZZGBM')
    sjsfxzzgbm = SFXZJGJBXX.objects.get(JGBM=sjsfxzzgbm_jgbm['JGBM'])
    if not sjsfxzzgbm:
      sjsfxzzgbm = None
    validated_data['SJSFXZZGBM'] = sjsfxzzgbm

    return SFXZJGJBXX.objects.create(**validated_data)


