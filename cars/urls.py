from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='car_list'),

    # ✅ أضف prefix واضح للتفاصيل
    path('car/<int:id>/', views.car_detail, name='car_detail'),

    path('book/<int:car_id>/', views.book_car, name='book_car'),
]
