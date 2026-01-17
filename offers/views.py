from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Offer

def offers_list(request):
    offers = Offer.objects.filter(is_active=True).order_by('-id')

    paginator = Paginator(offers, 9)  # ✅ عدد العروض في كل صفحة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'offers/offers_list.html', {
        'page_obj': page_obj
    })


def offer_detail(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    return render(request, 'offers/offer_detail.html', {
        'offer': offer
    })
