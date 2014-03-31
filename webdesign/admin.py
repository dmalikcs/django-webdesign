from django.contrib import admin
from webdesign.models import *


class DemoAdmin(admin.ModelAdmin):
    fields = ((),)
    list_display = ()
    list_filter = ()
    search_fields = ()

admin.site.register(Demo, DemoAdmin)
