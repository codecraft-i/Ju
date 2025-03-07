from django.shortcuts import render

# Local Modules
from .models import BotUser, UploadedFile
from .serializers import BotUserSerializer

from django.conf import settings

# Additional Modules
from rest_framework import serializers, viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action, api_view

import requests
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = "__all__"

class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

    @action(detail=True, methods=['post'])
    def upload_to_telegram(self, request, pk=None):
        """Faylni Telegram serveriga yuklash va file_id olish"""
        instance = self.get_object()
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendDocument"
        with open(instance.file.path, 'rb') as file_data:
            response = requests.post(url, data={"chat_id": settings.TELEGRAM_ADMIN_ID}, files={"document": file_data})
        
        if response.status_code == 200:
            file_id = response.json()["result"]["document"]["file_id"]
            instance.file_id = file_id
            instance.save()
            return Response({"file_id": file_id})
        return Response({"error": "Fayl yuklab bo‘lmadi"}, status=400)

    @action(detail=False, methods=['get'])
    def active_files(self, request):
        """Admin tomonidan faollashtirilgan fayllarni olish"""
        active_files = UploadedFile.objects.filter(is_active=True)
        serializer = self.get_serializer(active_files, many=True)
        return Response(serializer.data)

class BotUserListCreateView(generics.ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    permission_classes = [AllowAny]

class BotUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    permission_classes = [AllowAny]

@api_view(['GET'])
def is_user_exists(request, tg_user_id):
    """Foydalanuvchi bazada bor yoki yo‘qligini tekshiradi"""
    exists = BotUser.objects.filter(tg_user_id=tg_user_id).exists()
    return Response({"exists": exists})

@action(detail=False, methods=['get'])
def active_files(self, request):
    """Admin tomonidan faollashtirilgan fayllarni olish"""
    active_files = UploadedFile.objects.filter(is_active=True)
    serializer = self.get_serializer(active_files, many=True)
    return Response(serializer.data)