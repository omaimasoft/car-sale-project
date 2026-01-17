from django.contrib import admin
from .models import Offer, OfferImage


class OfferImageInline(admin.TabularInline):
    model = OfferImage
    extra = 3


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'new_price',
        'is_active',
        'is_expired',
        'end_date',
        'created_at',
    )

    list_filter = ('is_active',)
    search_fields = ('title', 'car_name')
    date_hierarchy = 'end_date'

    inlines = [OfferImageInline]
