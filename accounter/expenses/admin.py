from django.contrib import admin
from .models import ExpensesNote

class ExpensesNoteAdmin(admin.ModelAdmin):
    list_display = ('id','user','score','where_from')
    list_display_links = ('id','user','score','where_from')


admin.site.register(ExpensesNote,ExpensesNoteAdmin)