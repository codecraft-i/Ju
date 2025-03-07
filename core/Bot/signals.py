from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UploadedFile
import requests

@receiver(post_save, sender=UploadedFile)
def upload_to_telegram_after_save(sender, instance, created, **kwargs):
    if created and not instance.file_id:
        TELEGRAM_BOT_TOKEN = "8078632105:AAF_Mo_AkruTv0WZkmG91G_7HBObofHRwTM"
        TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"

        with open(instance.file.path, "rb") as f:
            response = requests.post(TELEGRAM_API_URL, data={"chat_id": "6122258979"}, files={"document": f})

        if response.status_code == 200:
            instance.file_id = response.json()["result"]["document"]["file_id"]
            instance.save()