from django.contrib import admin
from .models import OneNote

class IncomeNote(admin.ModelAdmin):
    list_display = ('id','user','score','where_from')
    list_display_links = ('id','user','score','where_from')


admin.site.register(OneNote,IncomeNote)
