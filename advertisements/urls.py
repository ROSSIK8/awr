from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import AdvertisementViewSet, sample_view

router = DefaultRouter()
router.register('advertisements', AdvertisementViewSet)


urlpatterns = [
    path('test', sample_view, name='test'),
] + router.urls
