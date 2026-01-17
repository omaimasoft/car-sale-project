from django.db import models
from django.utils import timezone
class Offer(models.Model):

    # ================= BASIC INFO =================
    title = models.CharField(max_length=200)
    car_name = models.CharField(max_length=200)

    # ================= MEDIA =================
    image = models.ImageField(upload_to='offers/')

    # ================= DESCRIPTION (NEW) =================
    description = models.TextField(
        verbose_name="وصف العرض",
        blank=True
    )

    # ================= PRICES =================
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)

    # ================= RATING (NEW) =================
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=5.0,
        verbose_name="التقييم"
    )

    # ================= TIME =================
    end_date = models.DateTimeField()

    # ================= STATUS =================
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "عرض"
        verbose_name_plural = "العروض"

    def __str__(self):
        return f"{self.title} - {self.car_name}"

    # ================= LOGIC =================
    def is_expired(self):
        return timezone.now() > self.end_date

    is_expired.boolean = True
    is_expired.short_description = "منتهي؟"

    def remaining_time(self):
        if self.is_expired():
            return "انتهى العرض"
        delta = self.end_date - timezone.now()
        return f"{delta.days} يوم / {delta.seconds // 3600} ساعة"
    def discount_percent(self):
        if self.old_price > 0:
         return round(
            ((self.old_price - self.new_price) / self.old_price) * 100
        )
        return 0
class OfferImage(models.Model):
    offer = models.ForeignKey(
        Offer,
        related_name='gallery',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='offers/gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"صورة - {self.offer.title}"
