# from django.urls import path
#
# from rest_framework import routers
#
# from contracts import views as contractsViews
#
#
# router = routers.DefaultRouter()
#
# router.register(prefix=r'(?P<contract_slug>.+)/rental-rates', viewset=contractCashflowViews.RentalRateView, base_name="rental_rates")
# router.register(prefix=r'(?P<contract_slug>.+)/inflation-rate', viewset=contractsViews.AddInflationRate, base_name="inflation_rate")
# router.register(prefix=r'(?P<contract_slug>.+)/obligations', viewset=contractsViews.Obligations, base_name="obligations_details")
# router.register(prefix=r'(?P<contract_slug>.+)/obligation-approval', viewset=contractsViews.ObligationApproval, base_name="obligation_approval")
# router.register(prefix=r'(?P<contract_slug>.+)/financial-details', viewset=contractsViews.FinancialDetails, base_name="financial_details")
# urlpatterns = router.urls
#
# urlpatterns += [
#     path('<slug:contract_slug>/working-group-master-list/', contractRentalViews.WorkingGroupMemberMasterView.as_view({'get': 'list', 'post': 'post'}, ),),
#     path('<contract_slug>/invoices/<int:pk>/initiate-mail/', contractCashflowViews.InvoiceView.as_view({'get': 'initiate_invoice_mail'})),
#     path('<contract_slug>/invoices/<int:pk>/send-mail/', contractCashflowViews.InvoiceView.as_view({'post': 'send_invoice_mail'})),
#     path('<slug:contract_slug>/rental-file-upload/', view=contractCashflowViews.read_rental_file, name="rental_upload"),
#     path('<slug:contract_slug>/annual-ratio/', view=contractsViews.annual_ratio, name="rental_upload"),
# ]
#
#
# from django.urls import include, path
# from rest_framework import routers
# from .views import *
#
# router = routers.DefaultRouter()
# router.register(r'changerequest',ChangeRequestViewSet,basename='cr')
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('getdata/<str:characteristic>/', getCharData),
#     path('newQuote/', newQuote),
#     path('editQuote/',editQuote),
#     path('', include(router.urls)),
# ]