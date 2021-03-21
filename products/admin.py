from django.contrib import admin
from .models import Products, Offer


## Edit the proudct admin view
class ProductAdmin(admin.ModelAdmin):
    # specify columns to be visible in the listing of prodcts in the admin panel
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    # specify columns to be visible in the listing of prodcts in the admin panel
    list_display = ('code', 'discount', 'description')


# Register your models here. so that they can appear in the admin page
admin.site.register(Products, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
