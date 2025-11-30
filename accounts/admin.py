from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'role', 'is_approved', 'is_active']
    list_filter = ['role', 'is_approved', 'is_active']
    search_fields = ['username', 'email']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone', 'address', 'is_approved', 'profile_image')}),
    )
    
    actions = ['approve_sellers']
    
    def approve_sellers(self, request, queryset):
        queryset.filter(role='seller').update(is_approved=True)
        self.message_user(request, 'Selected sellers have been approved.')
    approve_sellers.short_description = 'Approve selected sellers'
