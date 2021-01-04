import task
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from task.views import LanguageViewSet, BorderViewSet, DetailsViewSet

router = routers.DefaultRouter()
router.register('language', LanguageViewSet, basename='language')
router.register('border', BorderViewSet, basename='border')
router.register('detail', DetailsViewSet, basename='detail')
# router.register('speak', SpeakViewSet, basename='speak')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('borders/<uuid:pk>/', task.views.BorderAPIViewTest.as_view(), name='api-border'),


]
