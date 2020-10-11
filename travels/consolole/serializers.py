import json

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from . models import TrAssets, TrConstants

from datetime import datetime


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class DateFormatChange(serializers.DateField):
    def to_representation(self, value):
        return datetime.strftime(value, '%d-%m-%Y')


class AssetSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TrAssets
        exclude = ('deleted_at', 'created_at', 'updated_at')

    def to_representation(self, instance):
        data = super(AssetSerializer, self).to_representation(instance)

        asset = TrConstants.objects.filter(constant_type='asset_type', value=instance.asset_type).first()

        if asset:
            data['asset'] = {"value": asset.value, "label": asset.label}
        else:
            data['asset'] = {}

        return data