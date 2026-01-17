
from django.urls import path
from .views import offers_list, offer_detail

app_name = "offers"

urlpatterns = [
    path('', offers_list, name='offers_list'),
    path('<int:pk>/', offer_detail, name='offer_detail'),
]
