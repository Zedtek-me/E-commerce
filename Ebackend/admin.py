from django.contrib import admin
from .models import VendorProfile, BuyerProfile, Product, Category

# registering my tables for view in the admin dashboard
admin.site.register([VendorProfile, BuyerProfile,Product, Category])
