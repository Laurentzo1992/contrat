from django.contrib import admin
from authentication.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name']
    search_fields = ['username', 'email', 'first_name']
    list_filter = ['username']
    list_per_page = 4
    
admin.site.register(User, UserAdmin)
# Register your models here.