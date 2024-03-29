import datetime
import django
from django.db import models
from django.db.models import Manager
from django.contrib.auth.models import User

# vendor's table
class VendorProfile(models.Model):
    vendor= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img= models.ImageField(blank=True, upload_to= 'vendor_image/', default='default.jpg')
    phone= models.CharField(max_length=15, blank= True, null=True)

    # address
    address= models.TextField(max_length=2000000,blank= True, null= True, default='Some address!')

    class Meta:
        permissions= [('can_edit_products','can edit products'),
                    ('can_view_products','can view products'),
                    ]
    
    def __str__(self):
        return self.vendor.username

    def get_vendor_name(self):
        name= self.vendor.username
        return name

    # def save(self,*args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.profile_img.path)
    #     thumb=(400,400)
    #     img.thumbnail(thumb)
    #     img.save(self.profile_img.path)

# buyer's table
class BuyerProfile(models.Model):
    buyer= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img= models.ImageField(blank=True, upload_to= 'buyer_image/', default='default.jpg')
    phone= models.CharField(max_length=15, blank= True, null=True)

    # address
    address= models.TextField(max_length=2000000,blank= True, null= True, default='Some address!')

    class Meta:
        permissions= [('can_view_products','can view products')]

    def __str__(self):
        return self.buyer.username

    def get_buyer_name(self):
        name= self.buyer.username
        return name

    # def save(self,*args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.profile_img.path)
    #     thumb=(400,400)
    #     img.thumbnail(thumb)
    #     img.save(self.profile_img.path)

# product's table referencing the users'(buyers and vendors) table, since both buyers and vendors are users
class Product(models.Model):
    buyer= models.ForeignKey(BuyerProfile, on_delete=models.CASCADE, null= True, blank=True)
    vendor= models.ForeignKey(VendorProfile, on_delete= models.CASCADE, null= True, blank= True)
    product_name= models.CharField(max_length=20000, blank= False, )
    product_image= models.ImageField(default='default.jpg', blank= True, upload_to='products/')
    description= models.TextField(max_length=2000000, null=True)
    price= models.FloatField(max_length=10, blank=False, default=0.00)
    sold= models.BooleanField(default=False)


    def __str__(self):
        return self.product_name

    # def save(self,*args, **kwargs):
    #     super().save()
    #     img = Image.open(self.product_image.path)
    #     thumb=(400,400)
    #     img.thumbnail(thumb)
    #     img.save(self.product_image.path)

# category Table for each product--> This would help later when I just need to display product categories only.
class Category(models.Model):
    product=models.OneToOneField(Product, on_delete=models.CASCADE)
    category= models.CharField(max_length=100, blank= False)

    def __str__(self):
        return self.category

    # category manager
    productType= Manager()


class PurchasedProducts(models.Model):
    product= models.OneToOneField(Product, on_delete=models.CASCADE, blank= False, null= False)
    quantity= models.SmallIntegerField(default=1, blank= False)
    owned_by= models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    bought_by= models.ForeignKey(BuyerProfile, on_delete=models.CASCADE)
    date= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return (
                    'Vendor %s\'s %s, purchased on %s, by %s' %(self.owned_by.vendor.username, self.product.product_name, self.date, self.bought_by)
                )