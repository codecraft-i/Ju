from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import BotUser, UploadedFile

class CustomAdminSite(AdminSite):
    site_header = "Custom Bot Admin"
    site_title = "Custom Bot Admin Panel"
    index_title = "Welcome to Custom Bot Admin"

custom_admin_site = CustomAdminSite(name="custom_admin")

class CustomBotUserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "phone_number", "is_logged_in")
    search_fields = ("username", "phone_number")
    list_filter = ("is_logged_in",)

class CustomUploadedFileAdmin(admin.ModelAdmin):
    list_display = ("file_name", "file_id", "uploaded_at")
    search_fields = ("file_name",)
    list_filter = ("uploaded_at",)

try:
    custom_admin_site.register(BotUser, CustomBotUserAdmin)
    custom_admin_site.register(UploadedFile, CustomUploadedFileAdmin)
except admin.sites.AlreadyRegistered:
    pass  # Model allaqachon ro‘yxatdan o‘tgan bo‘lsa, xatolik yuzaga kelmasligi uchun