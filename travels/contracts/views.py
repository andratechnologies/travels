from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.response import Response
from . models import Contractor,Contract, Invoice, Maintainance
from .serializers import ContractorSerializer, ContractSerializer, InvoiceSerializer, MaintainanceSerializer
from travels import constants
from consolole import validation


def check_contract(request_function):

    def wrap(request, *args, **kwargs):
        contract = Contract.objects.filter(slug=kwargs['contract_slug']).first()
        if contract:
            request.kwargs['contract'] = contract
            return request_function(request, *args, **kwargs)
        else:
            response = {}
            response['data'] = {}
            if request.action == "list":
                response['data'] = []
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['status'] = constants.FAIL_STATUS
            response['message'] = "Required Contract Invalid or Missing!"
            return Response(response)

    return wrap



class ContractorViewSet(viewsets.ModelViewSet):
    serializer_class = ContractorSerializer
    queryset = Contractor.objects.all()



class VehicleContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
            return Contract.objects.all()

    def create(self, request, *args, **kwargs):
        response = {}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response["data"] = serializer.data
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Contract Created Successfully"
        else:
            response['message'] = validation.error_message(serializer).data["message"]
            response['data'] = {}
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['status'] = constants.FAIL_STATUS

        return Response(response)


    def list(self, request, *args, **kwargs):
        response = {}
        response['data'] = {}
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data)
        if len(serializer.data) > 0:
            for i in serializer.data:
                response['data'].update(i)
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Fetched Contract Details Successfully"
        else:
            response['status'] = constants.FAIL_STATUS
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['message'] = "No Contract Details Available"

        return Response(response)


    def retrieve(self, request, *args, **kwargs):
        response = {}
        response['data'] = {}
        if Contract.objects.filter(id=self.kwargs['pk']).exists():
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response['data'].update(serializer.data)
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Fetched Contract Details Successfully"
        else:
            response['status'] = constants.FAIL_STATUS
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['message'] = "Requested Contract Details are not valid"
        return Response(response)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        response = {}
        response['data'] = {}
        if Contract.objects.filter(id=self.kwargs['pk']).exists():
            instance = self.get_object()
            serializer = self.get_serializer(instance, partial=partial, data=request.data)
            if serializer.is_valid():
                self.perform_update(serializer)
                response['data'].update(serializer.data)
                response['statusCode'] = constants.SUCCESS_STATUS_CODE
                response['status'] = constants.SUCCESS_STATUS
                response['message'] = "Updated Contract Details Successfully"
                return Response(response)
            else:
                response['statusCode'] = constants.INVALID_STATUS_CODE
                response['status'] = constants.FAIL_STATUS
                response['message'] = validation.error_message(serializer).data["message"]
        return Response(response)


    def destroy(self, request, *args, **kwargs):
        response = {}
        if Contract.objects.filter(id=self.kwargs['pk']).exists():
            instance = self.get_object()
            self.perform_destroy(instance)
            response["data"] = {}
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Deleted Contract Successfully"
        else:
            response['data'] = {}
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['status'] = constants.FAIL_STATUS
            response['message'] = "Requested Contract Details is not valid"
        return Response(response)



class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
            queryset = Invoice.objects.all()

    @check_contract
    def create(self, request, *args, **kwargs):
        response = {}
        request.data['contract'] = self.kwargs['contract'].id
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response["data"] = serializer.data
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Invoice Created Successfully"
        else:
            response['message'] = validation.error_message(serializer).data["message"]
            response['data'] = {}
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['status'] = constants.FAIL_STATUS

        return Response(response)

    # @check_contract
    def list(self, request, *args, **kwargs):
        response = {}
        response['data'] = {}
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data)
        if len(serializer.data) > 0:
            for i in serializer.data:
                response['data'].update(i)
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Fetched Invoice Details Successfully"
        else:
            response['status'] = constants.FAIL_STATUS
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['message'] = "No Invoice Details Available"

        return Response(response)

    # @check_contract
    def retrieve(self, request, *args, **kwargs):
        response = {}
        response['data'] = {}
        # request.data['contract'] = self.kwargs['contract'].id
        if Invoice.objects.filter(id=self.kwargs['pk']).exists():
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response['data'].update(serializer.data)
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Fetched Invoice Details Successfully"
        else:
            response['status'] = constants.FAIL_STATUS
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['message'] = "Requested Invoice Details are not valid"
        return Response(response)

    @check_contract
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        response = {}
        request.data['contract'] = self.kwargs['contract'].id
        response['data'] = {}
        if Invoice.objects.filter(id=self.kwargs['pk']).exists():
            instance = self.get_object()
            serializer = self.get_serializer(instance, partial=partial, data=request.data)
            if serializer.is_valid():
                self.perform_update(serializer)
                response['data'].update(serializer.data)
                response['statusCode'] = constants.SUCCESS_STATUS_CODE
                response['status'] = constants.SUCCESS_STATUS
                response['message'] = "Updated Invoice Details Successfully"
                return Response(response)
            else:
                response['statusCode'] = constants.INVALID_STATUS_CODE
                response['status'] = constants.FAIL_STATUS
                response['message'] = validation.error_message(serializer).data["message"]
        return Response(response)

    # @check_contract
    def destroy(self, request, *args, **kwargs):
        response = {}
        # request.data['contract'] = self.kwargs['contract'].id
        if Invoice.objects.filter(id=self.kwargs['pk']).exists():
            instance = self.get_object()
            self.perform_destroy(instance)
            response["data"] = {}
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Deleted Invoice Successfully"
        else:
            response['data'] = {}
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['status'] = constants.FAIL_STATUS
            response['message'] = "Requested Invoice Details is not valid"
        return Response(response)


class MaintainanceViewSet(viewsets.ModelViewSet):
    serializer_class = MaintainanceSerializer
    queryset = Maintainance.objects.all()