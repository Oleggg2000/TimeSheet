from django.contrib import admin

from .models import Records, Customer

admin.site.register(Customer)
admin.site.register(Records)
