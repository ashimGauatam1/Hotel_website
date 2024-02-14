from django.contrib import admin
from home.models import Contact,bookr,register_customer

# Register your models here.

admin.site.register(Contact)
admin.site.register(bookr)
admin.site.register(register_customer)