from django.contrib import admin
from .models import Service,Category,Tag,RequestedService

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug','name_fa','name_en')
 
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(RequestedService)
class RequestedServiceAdmin(admin.ModelAdmin):
    pass