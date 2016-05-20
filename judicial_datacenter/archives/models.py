# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel,TreeForeignKey

# Create your models here.


# ref GB/T 2260-2007 行政区划
class XZQH(MPTTModel):
  code = models.CharField(max_length=6,verbose_name="编码")
  text = models.CharField(max_length=20,verbose_name="名称")  
  note = models.CharField(max_length=20,verbose_name="说明",blank=True,null=True)
  parent = TreeForeignKey("self",null=True,blank=True,related_name='children',db_index=True)

  def __unicode__(self):
    return self.text

  class Meta:
    verbose_name = "行政区划" 
    verbose_name_plural = "行政区划"

  class MPTTMeta:
    order_insertion_by = ['code']


# ref SF 05001-2013 unit 8.2 机构类别
class JGLB(MPTTModel):
  code = models.CharField(max_length=4,verbose_name="编码")
  text = models.CharField(max_length=20,verbose_name="名称")
  note = models.CharField(max_length=20,verbose_name="说明",blank=True,null=True)
  parent = TreeForeignKey("self",null=True,blank=True,related_name='children',db_index=True)

  def __unicode__(self):
    return self.text

  class Meta:
    verbose_name = "机构类别"
    verbose_name_plural = "机构类别"

  class MPTTMeta:
    order_insertion_by = ['code']


# ref SF 05001-2013 unit 8.3 机构隶属层级
class JGLSCJ(models.Model):
  code = models.CharField(max_length=2,verbose_name="编码")
  text = models.CharField(max_length=20,verbose_name="名称")
  parent_code = models.CharField(max_length=2,verbose_name="上级编码",blank=True,null=True)
  note = models.CharField(max_length=20,verbose_name="说明",blank=True,null=True)

  def __unicode__(self):
    return self.text

  class Meta:
    verbose_name = "机构隶属层级"
    verbose_name_plural = "机构隶属层级"

# ref SF 05001-2013 unit 8.4 机构行政级别
class JGXZJB(models.Model):
  code = models.CharField(max_length=2,verbose_name="编码")
  text = models.CharField(max_length=20,verbose_name="名称")
  parent_code = models.CharField(max_length=2,verbose_name="上级编码",blank=True,null=True)
  note = models.CharField(max_length=20,verbose_name="说明",blank=True,null=True)

  def __unicode__(self):
    return self.text

  class Meta:
    verbose_name = "机构行政级别"
    verbose_name_plural = "机构行政级别"


# ref SF 05001-2013 unit 7.1 司法行政机关（单位）基本信息采集表
class SFXZJGJBXX(MPTTModel):
  JGBM  = models.CharField(max_length=18,verbose_name="机构编码")
  JGMC  = models.CharField(max_length=60,verbose_name="机构名称")
  JGJC  = models.CharField(max_length=60,verbose_name="机构简称",blank=True,null=True)
  YWMC  = models.CharField(max_length=60,verbose_name="英文名称",blank=True,null=True)
  JGDM  = models.CharField(max_length=20,verbose_name="机构代码")
  FZR   = models.CharField(max_length=20,verbose_name="负责人",blank=True,null=True)
  JGLB  = models.ForeignKey(JGLB,verbose_name="机构类别") 
  JGXZJB  = models.ForeignKey(JGXZJB,verbose_name="机构行政级别",blank=True,null=True)
  JGLSCJ  = models.ForeignKey(JGLSCJ,verbose_name="机构隶属层级")
  #SJSFXZZGJG  = models.CharField(max_length=16,verbose_name="上级司法行政主管机关",blank=True,null=True)
  SJSFXZZGJG = TreeForeignKey('self',null=True,blank=True,related_name='sjsfxzzgjg_children',db_index=True)
  #SJSFXZZGBM  = models.CharField(max_length=16,verbose_name="上级司法行政主管部门",blank=True,null=True)
  SJSFXZZGBM = TreeForeignKey('self',null=True,blank=True,related_name='sjsfxzzgbm_children',db_index=True)
  LXDH  = models.CharField(max_length=40,verbose_name="联系电话",blank=True,null=True)
  CZHM  = models.CharField(max_length=40,verbose_name="传真号码",blank=True,null=True)
  DZYX  = models.CharField(max_length=60,verbose_name="电子邮箱",blank=True,null=True)
  YB  = models.CharField(max_length=6,verbose_name="邮编",blank=True,null=True)
  DZ  = models.CharField(max_length=200,verbose_name="地址",blank=True,null=True)

  def __unicode__(self):
    return self.JGMC

  class Meta:
    verbose_name = "司法行政机关基本信息"
    verbose_name_plural = "司法行政机关基本信息"

  class MPTTMeta:
    parent_attr = 'SJSFXZZGJG'
    order_insertion_by = ['JGBM']



