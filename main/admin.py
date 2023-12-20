from django.contrib import admin
from main.models import ItemModels
# Register your models here.


@admin.register(ItemModels)
class ItemModelsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name', )
    readonly_fields = ('price_warning', 'item_token',)