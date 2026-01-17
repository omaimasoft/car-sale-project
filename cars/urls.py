from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.car_list, name='car_list'),
#     path('book/<int:car_id>/', views.book_car, name='book_car'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ✅ استخدم home وليس slider_voitures
    path('cars/', views.car_list, name='car_list'),
    path('<int:id>/', views.car_detail, name='car_detail'),
    path('book/<int:car_id>/', views.book_car, name='book_car'),
]
