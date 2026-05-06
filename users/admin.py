from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.ControlUsers)
class UserAdmin(admin.ModelAdmin):
    list_display=('username','first_name','last_name','email','phon','slug')
    list_display_links=('username',)
    list_editable=('phon',)
    search_fields=('frist_name','last_name' )
    readonly_fields=('slug',)
    list_filter=('email',)
    list_per_page=15
    
