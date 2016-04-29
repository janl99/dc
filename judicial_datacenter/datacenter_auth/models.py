# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class string_with_title(str):
  def __new__(cls,value,title):
    instance = str.__new__(cls,value)
    instance._title = title
    return instance

  def title(self):
    return self._title

  __copy__ = lambda self: self
  __deepcopy__ = lambda self, memodict: self

# Create your models here.

class DatacenterUser(AbstractUser):
  img = models.CharField(max_length=200,default='/static/tx/default.jpg',verbose_name=u'头像地址')
  intro = models.CharField(max_length=200,blank=True,null=True,verbose_name=u'简介')

  class Meta(AbstractUser.Meta):
    app_label =string_with_title('datacenter_auth',u"用户管理")



