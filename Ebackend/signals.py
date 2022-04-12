from django.db.models.signals import post_save
from .models import VendorProfile, BuyerProfile, Product
from django.contrib.auth.models import Group, Permission, User

# defining a callback for adding vendors to group
def add_to_vendor_group(sender, instance, created, **kwargs):
    if created:
        vendor_group= Group.objects.get(name='Vendors')
        instance.vendor.groups.add(vendor_group)
        instance.save()

# sending the signal from the vendorprofile table
post_save.connect(add_to_vendor_group, sender=VendorProfile, weak= False)