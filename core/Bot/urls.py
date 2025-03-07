from django.urls import path, include
# Local Modules
from .views import UploadedFileViewSet, BotUserListCreateView, BotUserDetailView, is_user_exists

# Additional Modules
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'files', UploadedFileViewSet)

generateUrlAPI = 'jklhgfr676tfyghjvbkjhvgfxdfgrsw43e56rt787y65r47ew3sredhgcfjgkhgvjfchdtruytiugyfcdhftgutfyurdytrfyjgvcghdtrfuytgiuyhiulyugityfurtfjgk'

urlpatterns = [
    path(f'{ generateUrlAPI }/', include(router.urls)),

    path(f'{ generateUrlAPI }/bot-users/', BotUserListCreateView.as_view(), name='bot-user-list'),
    path(f'{ generateUrlAPI }/bot-users/<int:pk>/', BotUserDetailView.as_view(), name='bot-user-detail'),
    path(f'{ generateUrlAPI }/isuser/<int:tg_user_id>/', is_user_exists, name='is-user-exists'),
]