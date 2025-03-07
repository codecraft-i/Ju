from django.contrib import admin

# Local Modules
from .models import BotUser, UploadedFile

# Register your models here.

@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('tg_user_id', 'username', 'first_name', 'last_name', 'phone_number', 'joined_at')
    search_fields = ('tg_user_id', 'username', 'first_name', 'last_name')
    ordering = ('-joined_at',)

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ("description", "is_active", "file", "file_id", "uploaded_at")
    list_filter = ("is_active", "uploaded_at")
    search_fields = ("file", "file_id")
    actions = ["mark_as_active", "mark_as_inactive"]

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)
    mark_as_active.short_description = "Tanlangan fayllarni faollashtirish"

    def mark_as_inactive(self, request, queryset):
        queryset.update(is_active=False)
    mark_as_inactive.short_description = "Tanlangan fayllarni sessiyani tugatish"