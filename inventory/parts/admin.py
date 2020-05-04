from django.contrib import admin
from work_orders.models import *
from .models import partslist
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class partsresource(resources.ModelResource):

    class Meta:
        model = partslist

class importparts(ImportExportModelAdmin):
    resource_class = partsresource

class jobsresource(resources.ModelResource):

    class Meta:
        model = jobs

admin.site.register(partslist, importparts)
admin.site.register(jobs)