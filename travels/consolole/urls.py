from django.urls import path, include

from rest_framework import routers

from . views import AssetDetailsViewSet

router = routers.DefaultRouter()
router.register(r'asset_details', AssetDetailsViewSet, basename='asset_details')
urlpatterns = router.urls

urlpatterns += [
    path('asset_data/', AssetDetailsViewSet),
    path('', include(router.urls)),
]