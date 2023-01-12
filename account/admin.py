from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_superuser', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_superuser', 'is_staff', 'is_active')


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
