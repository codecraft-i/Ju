from django.db import models

# Create your models here.

class BotUser(models.Model):
    tg_user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} (@{self.username})" if self.username else self.first_name
    
    class Meta:
        verbose_name = "Telegram Bot Foydalanuvchilari"
        verbose_name_plural = "Bot Foydalanuvchilari"

class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    file_id = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.file.name
    
    class Meta:
        verbose_name = "Telegram Bot Files"
        verbose_name_plural = "Files"