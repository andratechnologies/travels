from django.db import models

from django.db.models.query import QuerySet
from django.utils import timezone


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()


class TrConstants(SoftDeletionModel):
    constant_type = models.CharField(max_length=255)
    value = models.IntegerField()
    label = models.CharField(max_length=255)
    is_editable = models.BooleanField(default=0)
    is_visible = models.BooleanField(default=1)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        app_label = 'consolole'
        db_table = 'tr_constants'
        verbose_name = 'Constant'
        verbose_name_plural = 'constant'

    def __str__(self):
        return self.constant_type

class TrAssets(SoftDeletionModel):
    asset_type = models.IntegerField()
    asset_number = models.CharField(max_length=15)
    asset_model = models.IntegerField(blank=True, null=True)
    asset_value = models.IntegerField(default=100000, blank=True, null=True)
    model_expiry = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='media/asset_image', blank=True, null=True)
    insurance_expiry_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    class Meta:
        app_label = 'consolole'
        db_table = 'tr_assets'
        verbose_name = 'Assets'
        verbose_name_plural = 'assets'

    def __str__(self):
        return self.asset_type



