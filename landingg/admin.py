from django.contrib import admin
from .models import*
from landingg.models import site_visitor
from landingg.models import AlphaGuide
from import_export.admin import ImportExportModelAdmin
from embed_video.admin import AdminVideoMixin
from .models import AlphaGuide,NameField

admin.site.register(site_visitor)
admin.site.register(NameField)

class AlphaGuideAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
admin.site.register(AlphaGuide, AlphaGuideAdmin)
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass