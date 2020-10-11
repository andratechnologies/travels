from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.response import Response
from . models import TrConstants, TrAssets
from .serializers import AssetSerializer
from travels import constants
from consolole import validation


class AssetDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = AssetSerializer

    def get_queryset(self):
            return TrAssets.objects.all()

    def create(self, request, *args, **kwargs):
        response = {}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response["data"] = serializer.data
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Asset Created Successfully"
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
        if len(serializer.data) > 0:
            for i in serializer.data:
                response['data'].update(i)
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Fetched Asset Details Successfully"
        else:
            response['status'] = constants.FAIL_STATUS
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['message'] = "No Asset Details Available"

        return Response(response)


    def retrieve(self, request, *args, **kwargs):
        response = {}
        response['data'] = {}
        if TrAssets.objects.filter(id=self.kwargs['pk']).exists():
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response['data'].update(serializer.data)
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Fetched Asset Details Successfully"
        else:
            response['status'] = constants.FAIL_STATUS
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['message'] = "Requested Asset Details are not valid"
        return Response(response)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        response = {}
        response['data'] = {}
        if TrAssets.objects.filter(id=self.kwargs['pk']).exists():
            instance = self.get_object()
            serializer = self.get_serializer(instance, partial=partial, data=request.data)
            if serializer.is_valid():
                self.perform_update(serializer)
                response['data'].update(serializer.data)
                response['statusCode'] = constants.SUCCESS_STATUS_CODE
                response['status'] = constants.SUCCESS_STATUS
                response['message'] = "Updated Asset Details Successfully"
                return Response(response)
            else:
                response['statusCode'] = constants.INVALID_STATUS_CODE
                response['status'] = constants.FAIL_STATUS
                response['message'] = validation.error_message(serializer).data["message"]
        return Response(response)


    def destroy(self, request, *args, **kwargs):
        response = {}
        if TrAssets.objects.filter(id=self.kwargs['pk']).exists():
            instance = self.get_object()
            self.perform_destroy(instance)
            response["data"] = {}
            response['statusCode'] = constants.SUCCESS_STATUS_CODE
            response['status'] = constants.SUCCESS_STATUS
            response['message'] = "Deleted Asset Successfully"
        else:
            response['data'] = {}
            response['statusCode'] = constants.INVALID_STATUS_CODE
            response['status'] = constants.FAIL_STATUS
            response['message'] = "Requested Asset Details is not valid"
        return Response(response)