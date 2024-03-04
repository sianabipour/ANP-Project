from django.contrib import admin
from .models import Product,Category,Tag,Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug','name_fa','name_en')
 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass