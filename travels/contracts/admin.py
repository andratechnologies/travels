from django.contrib import admin

from . models import *

# Register your models here.

admin.site.register(Contract)
admin.site.register(Contractor)
admin.site.register(Invoice)
admin.site.register(Maintainance)