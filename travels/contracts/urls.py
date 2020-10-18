from django.urls import path, include

from rest_framework import routers

from . views import ContractorViewSet, VehicleContractViewSet, InvoiceViewSet, MaintainanceViewSet

router = routers.DefaultRouter()
router.register(r'contractor_details', ContractorViewSet, basename='contractor_details')
router.register(r'vehicle_contract_details', VehicleContractViewSet, basename='vehicle_contract')
router.register(r'(?P<contract_slug>.+)/invoice_details', InvoiceViewSet, basename='Invoice_deatils')
router.register(r'asset_maintaince', MaintainanceViewSet, basename='maintainance')
# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]