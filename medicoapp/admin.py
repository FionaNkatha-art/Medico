from django.contrib import admin
from medicoapp.models import Product, Company, Patient,Appointment,Member

# Register your models here.
admin.site.register(Product)
admin.site.register(Patient)
admin.site.register(Company)
admin.site.register(Appointment)
admin.site.register(Member)