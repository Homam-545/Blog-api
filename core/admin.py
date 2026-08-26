from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, BlogPost


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name',
                     'phone_number', 'is_staff', 'is_active', 'created_at']
    list_filter = ['is_staff', 'is_active', 'created_at']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']
    ordering = ['-created_at']

    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات تکمیلی', {'fields': ('phone_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('اطلاعات تکمیلی', {'fields': ('phone_number', 'email', 'first_name', 'last_name')}),
    )
    readonly_fields = ['created_at', 'updated_at']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'content', 'author__username']
    list_editable = ['status']
    autocomplete_fields = ['author']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    actions = ['approve_posts', 'reject_posts']

    @admin.action(description='approve_posts')
    def approve_posts(self, request, queryset):
        updated = queryset.update(status=BlogPost.Status.PUBLISHED)
        self.message_user(request, f'{updated}post approved')

    @admin.action(description='reject_posts')
    def reject_posts(self, request, queryset):
        updated = queryset.update(status=BlogPost.Status.REJECTED)
        self.message_user(request, f'{updated} post rejected.')
