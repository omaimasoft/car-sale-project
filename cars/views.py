from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Booking
from offers.models import Offer  
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import render
from .models import Voiture
import re

def car_list(request):
    cars = Car.objects.all().order_by('-id')  # ✅ كل السيارات

    paginator = Paginator(cars, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cars/car_list.html', {
        'page_obj': page_obj
    })



def book_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()

        # ✅ التحقق من رقم الهاتف (10 أرقام فقط)
        if not re.fullmatch(r"\d{10}", phone):
            messages.error(
                request,
                "❌ رقم الهاتف يجب أن يتكون من 10 أرقام فقط"
            )
            return render(request, "cars/book_car.html", {"car": car})

        # ✅ منع الإرسال المكرر (نفس السيارة + نفس الهاتف)
        already_exists = Booking.objects.filter(
            car=car,
            phone=phone
        ).exists()

        if already_exists:
            messages.warning(
                request,
                "⚠️ لقد قمت بإرسال طلب حجز لهذه السيارة من قبل"
            )
            return redirect("book_car", car_id=car.id)

        # ✅ حفظ الطلب
        Booking.objects.create(
            car=car,
            name=name,
            phone=phone
        )

        # ✅ رسالة نجاح
        messages.success(
            request,
            "✅ تم إرسال طلب الحجز بنجاح، سيتم التواصل معك قريبًا"
        )

        # 🔒 POST → REDIRECT → GET (يمنع التكرار)
        return redirect("book_car", car_id=car.id)

    return render(request, "cars/book_car.html", {"car": car})

def home(request):
    cars = Car.objects.filter(status='available')[:3]

    # 🔥 آخر عرضين مضافين (الأحدث أولاً)
    offers = Offer.objects.filter(is_active=True).order_by('-created_at')[:2]

    # آخر السيارات
    voitures = Voiture.objects.all().order_by('-created_at')

    return render(request, 'cars/home.html', {
        'cars': cars,
        'offers': offers,
        'voitures': voitures
    })
def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'cars/car_detail.html', {'car': car})
