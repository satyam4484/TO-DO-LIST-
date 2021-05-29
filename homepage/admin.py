from django.contrib import admin
from .models import todomodel
# Register your models here.

@admin.register(todomodel)
class todoadmin(admin.ModelAdmin):
    list_display = ('user','title','desc','startdate','enddate')