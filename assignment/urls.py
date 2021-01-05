from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from task.views import LanguageViewSet, BorderViewSet, DetailsViewSet, CountryListView, SearchResultsView, \
    CountryDetailsView

router = routers.DefaultRouter()
router.register('language', LanguageViewSet, basename='language')
router.register('border', BorderViewSet, basename='border')
router.register('detail', DetailsViewSet, basename='detail')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('country/', CountryListView.as_view(), name='country'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('search/details/', CountryDetailsView.as_view(), name='details')

]
