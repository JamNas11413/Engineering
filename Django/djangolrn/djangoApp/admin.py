from django.contrib import admin
from .models import Products
from .models import Customers
from .models import Orders



# customizing the list page:  
#     like add new columns and make it editible etc

@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin): # we could call it anything but convention is that we use name of the model and followed by word Admin # here we can define the how we wants to view our products
    list_display = ['title', 'price', 'inventory_status']
    list_editable('price')
    list_per_page = 10

    # adding computed columns like inventory = here + there etc
    @admin.display(ordering='inventory')  # to apply sorting 
    def inventory_status(self, product):
            if product.inventory < 10:
                 return 'low'
        
            return 'OK'

    # TO SEE THE COMPLETE LIST OF OPETIONS WE CAN SET HERE, JUST GOOGLE
    # Django ModelAdmin -> model admin,options

@admin.register(models.Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','membership']
    list_editable('membership')
    ordering=['first_name','last_name']
    list_per_page = 10



@admin.register(models.Orders)
class OrderAdmin(admin.ModelAdmin):
     list_display = ['id', 'place_at', 'customer']



# Register your models here.

# admin.site.register(Customers)
# admin.site.register(Products, ProductAdmin)  # we have to pass it the model in order to be applied on OR WE CAN USE THE DECORATER AND THEN WE NOT NEED THIS REGISTERATION STATEMENT AS WELL