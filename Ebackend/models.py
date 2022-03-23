from django.db import models
from django.contrib.auth.models import User, Permission
from PIL import Image

# vendor's table
class VendorProfile(models.Model):
    vendor= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img= models.ImageField(blank=True, upload_to= 'vendor_image/', default='default.jpg')

    class Meta:
        permissions= [('can_edit_products','can edit products'),
                    ('can_view_products','can view products'),
                    ]
    
    def __str__(self):
        return self.vendor

    # def save(self,*args, **kwargs):
    #     super().save()
    #     img = Image.open(self.profile_img.path)
    #     thumb=(400,400)
    #     img.thumbnail(thumb)
    #     img.save()

# buyer's table
class BuyerProfile(models.Model):
    buyer= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img= models.ImageField(blank=True, upload_to= 'buyer_image/', default='default.jpg')

    class Meta:
        permissions= [('can_view_products','can view products')]

    def __str__(self):
        return self.buyer

    # def save(self,*args, **kwargs):
    #     super().save()
    #     img = Image.open(self.profile_img.path)
    #     thumb=(400,400)
    #     img.thumbnail(thumb)
    #     img.save()

# product's table referencing the user table, since both buyers and vendors are sellers
class Product(models.Model):
    buyer= models.ForeignKey(BuyerProfile, on_delete=models.CASCADE, null= True, blank=True)
    vendor= models.ForeignKey(VendorProfile, on_delete= models.CASCADE, null= True, blank= True)
    product_name= models.CharField(max_length=20000, blank= False, )
    product_image= models.ImageField(default='default.jpg', blank= True, upload_to='products/', null=True)
    description= models.TextField(max_length=2000000, null=True)
    price= models.FloatField(max_length=10, blank=False, default=0.00)


    def __str__(self):
        return self.product_name

    # def save(self,*args, **kwargs):
    #     super().save()
    #     img = Image.open(self.product_image.path)
    #     thumb=(400,400)
    #     img.thumbnail(thumb)
    #     img.save()