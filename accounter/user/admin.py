from django.contrib import admin

from .models import CustomUser,Photo

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email','first_name','last_name')
    list_display_links = ('id','email','first_name','last_name')
    list_filter = ('id','email','is_staff')
    search_fields = ('email','first_name','last_name')
    ordering = ('email',)

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Photo)
