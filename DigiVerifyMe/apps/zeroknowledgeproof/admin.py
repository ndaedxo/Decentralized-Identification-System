# admin.py

from django.contrib import admin
from .models import ZKPSettings, ZKPRecord

admin.site.register(ZKPSettings)
admin.site.register(ZKPRecord)
