from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from .models import JGLB,JGLSCJ,JGXZJB,SFXZJGJBXX
# Register your models here.

class CustomMPTTModelAdmin(MPTTModelAdmin):
  mptt_level_indent = 20

admin.site.register(JGLB,CustomMPTTModelAdmin)
admin.site.register(JGLSCJ)
admin.site.register(JGXZJB)
admin.site.register(SFXZJGJBXX)
