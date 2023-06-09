from django.contrib import admin
from . models import prof

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'bca', 'mca', 'lang', 'tenth', 'twelth')

# Register your models here.
admin.site.register(prof, ProfileAdmin)