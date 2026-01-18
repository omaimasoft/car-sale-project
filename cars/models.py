from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.urls import reverse


class Car(models.Model):

    FUEL_CHOICES = [
        ('diesel', 'Diesel'),
        ('gasoline', 'Gasoline'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
    ]

    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
    ]

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('sold', 'Sold'),
    ]

    # المعلومات الأساسية
    brand = models.CharField(max_length=100, verbose_name="الماركة")
    model = models.CharField(max_length=100, verbose_name="الموديل")
    year = models.PositiveIntegerField(verbose_name="سنة الصنع")

    # المواصفات
    mileage = models.PositiveIntegerField(verbose_name="الكيلومتراج (كم)")
    power = models.CharField(max_length=50, verbose_name="القوة (حصان)")
    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES,
        verbose_name="نوع الوقود"
    )
    transmission = models.CharField(
        max_length=20,
        choices=TRANSMISSION_CHOICES,
        verbose_name="ناقل الحركة"
    )
    doors = models.PositiveSmallIntegerField(verbose_name="عدد الأبواب")

    # الحالة والسعر
    condition = models.CharField(
        max_length=10,
        choices=CONDITION_CHOICES,
        verbose_name="الحالة"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر"
    )

    # الوصف
    description = models.TextField(verbose_name="الوصف")

    # الصورة الرئيسية
    image = models.ImageField(
        upload_to='cars/',
        verbose_name="الصورة الرئيسية"
    )

    # حالة الإعلان
    status = models.CharField(
    max_length=10,
    choices=STATUS_CHOICES,
    default='available',
    verbose_name="حالة الإعلان"
)

    def __str__(self):
            return f"{self.brand} {self.model} ({self.year})"
    def get_absolute_url(self):
        return reverse('car_detail', args=[self.id])

    created_at = models.DateTimeField(auto_now_add=True)
class CarImage(models.Model):
    car = models.ForeignKey(
        Car,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='cars/gallery/')

    def __str__(self):
        return f"Image for {self.car}"


class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.car.brand} {self.car.model}"


# @receiver(post_save, sender=Booking)
# def change_car_status(sender, instance, **kwargs):
#     if instance.confirmed:
#         instance.car.status = 'reserved'
#         instance.car.save()


# models.py
from django.db import models

class Voiture(models.Model):
    image = models.ImageField(upload_to='voitures/')
    marque = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.marque
