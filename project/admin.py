from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["slug","name_fa","name_en","size","order_number"]
    list_editable = ["order_number","size"]