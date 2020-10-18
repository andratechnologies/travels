import json

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from consolole.models import TrConstants, TrAssets
from . models import Contractor, Contract, Invoice, Maintainance
from consolole.serializers import DynamicFieldsModelSerializer

from datetime import datetime



class ContractorSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Contractor
        exclude = ('created_at', 'updated_at')


class ContractSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Contract
        exclude = ('created_at', 'updated_at')

    def to_representation(self, instance):
        data = super(ContractSerializer, self).to_representation(instance)
        contractor = Contractor.objects.filter(name=instance.contractor).first()
        asset = TrAssets.objects.filter(id=instance.asset_id).first()

        if contractor:
            data['contractor'] = {"name": contractor.name, "email": contractor.email}
        else:
            data['contractor'] = {}

        if asset:
            data['asset'] = {"vehicle_number": asset.asset_number}
        else:
            data['asset'] = {}

        return data


class InvoiceSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Invoice
        exclude = ('created_at', 'updated_at')

    def to_representation(self, instance):
        data = super(InvoiceSerializer, self).to_representation(instance)
        contract = Contract.objects.filter(id=instance.contract_id).first()
        contractor = Contractor.objects.filter(id=contract.contractor_id).first()

        if contractor:
            data['contract'] = {"contractor": contractor.name, "email": contractor.email}
        else:
            data['contract'] = {}

        return data

class MaintainanceSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Maintainance
        exclude = ('created_at', 'updated_at')

    def to_representation(self, instance):
        data = super(MaintainanceSerializer, self).to_representation(instance)
        contract = Contract.objects.filter(id=instance.contract_id).first()
        contractor = Contractor.objects.filter(id=contract.contractor_id).first()

        if contractor:
            data['contract'] = {"contractor": contractor.name, "email": contractor.email}
        else:
            data['contract'] = {}

        return data