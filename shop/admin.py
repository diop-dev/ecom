from django.contrib import admin
from .models import Category, Product, Commande


# Register your models here.

admin.site.site_header ="E-commerce"
admin.site.site_title= "MO shop"
admin.site.index_title = "Développeur Wep"


class AdminProduct(admin.ModelAdmin):
    list_display = ['title','price','category' ,'date_added'] 
    search_fields = ('title',)
    list_editable= ('price',)
    
    
    def get_category(self,obj):
        return obj.category.name 
    get_category.short_description= "Category"

class  AdminCommande (admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'address', 'ville','pays','total', 'date_commande' )
        
        
admin.site.register(Category)
admin.site.register(Product, AdminProduct)
admin.site.register(Commande, AdminCommande)



