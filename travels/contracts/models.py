from django.db import models
from django_extensions.db.fields import RandomCharField

from consolole import models as consoleModels



class Contractor(consoleModels.SoftDeletionModel):
    name = models.CharField(max_length=100)
    contact_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    address = models.TextField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        app_label = 'contracts'
        db_table = 'tr_contractor'
        verbose_name = 'Contractor'
        verbose_name_plural = 'contractor'

    def __str__(self):
        return self.name



class Contract(consoleModels.SoftDeletionModel):
    slug = RandomCharField(length=6, include_digits=False, unique=True)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    rental_amount = models.FloatField(blank=True, null=True)
    asset = models.ForeignKey(consoleModels.TrAssets, on_delete=models.CASCADE, related_name="contract_asset")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        app_label = 'contracts'
        db_table = 'tr_contract'
        verbose_name = 'Contracts'
        verbose_name_plural = 'contracts'

    def __str__(self):
        return self.slug


class Invoice(consoleModels.SoftDeletionModel):
    slug = RandomCharField(length=6, include_digits=False, unique=True)
    invoice_date = models.DateField(auto_now_add=True, blank=True, null=True)
    invoice_month = models.CharField(max_length=10,blank=True, null=True)
    Due_date = models.DateField()
    invoice_amount = models.FloatField(blank=True, null=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="contract_invoice")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        app_label = 'contracts'
        db_table = 'tr_invoice'
        verbose_name = 'Invoice'
        verbose_name_plural = 'invoice'

    def __str__(self):
        return self.slug



class Maintainance(consoleModels.SoftDeletionModel):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="contract_maintainance")
    monthly_rate = models.FloatField()
    max_km = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    class Meta:
        app_label = 'contracts'
        db_table = 'tr_maintainance'
        verbose_name = 'Maintainance'
        verbose_name_plural = 'maintainance'

    def __str__(self):
        return self.monthly_rate




