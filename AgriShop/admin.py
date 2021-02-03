from django.contrib import admin
from AgriShop.models import Manufacturer, User, Product, InOrder
from django.utils import timezone


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'in_stock', 'manufacturer', 'photo']
    ordering = ['name']


def make_done(modeladmin, request, queryset):
    for inorder in queryset:
        inorder.status = 'arrived'
        inorder.arrive_date = timezone.now()
        inorder.product.in_stock += inorder.amount
        inorder.product.save()
        inorder.save()


make_done.short_description = "Product arrived"


@admin.register(InOrder)
class InOrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'amount', 'arrive_date', 'status', 'get_time']
    ordering = ['-status', 'product']
    fields = ("product", "amount", "arrive_date","invoice")
    actions = [make_done]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'telephone', 'is_staff', 'last_login']
    ordering = ['username', 'last_login']
    list_filter = ("is_staff",)
    fields = ("username", "email", "telephone")
    search_fields = ("username__startswith", "telephone__startswith", "email__startswith")


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'representative_name', 'telephone']
    ordering = ['name']

# Register your models here.
