from django.contrib import admin
from django.utils.html import format_html
from .models import Car, CarImage, Booking


# =========================
# Inline Images for Car
# =========================
class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1


# =========================
# Car Admin
# =========================
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'model',
        'year',
        'price',
        'status',
        'condition',
        'image_preview',
    )

    list_filter = ('status', 'fuel_type', 'transmission', 'condition')
    search_fields = ('brand', 'model')
    inlines = [CarImageInline]

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="90" style="border-radius:8px;" />',
                obj.image.url
            )
        return "—"

    image_preview.short_description = "الصورة"


# =========================
# Booking Admin (WITH IMAGE)
# =========================
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'car',
        'car_image',
        'confirmed',
        'created_at',
    )

    list_filter = ('confirmed',)
    search_fields = ('name', 'phone', 'car__brand', 'car__model')
    readonly_fields = ('car_image',)

    def car_image(self, obj):
        if obj.car and obj.car.image:
            return format_html(
                '<img src="{}" width="120" style="border-radius:10px;" />',
                obj.car.image.url
            )
        return "لا توجد صورة"

    car_image.short_description = "صورة السيارة"
