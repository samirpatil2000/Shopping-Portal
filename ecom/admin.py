from django.contrib import admin
from .models import ProductInCart,Product,Order,Category
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductInCart)
admin.site.register(Order)

admin.site.register(Category)


#TODO Tasks
#Checkout
#Favourites
