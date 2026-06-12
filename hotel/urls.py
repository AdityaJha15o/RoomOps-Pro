from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('rooms/', views.rooms, name='rooms'),

    path('booking/', views.booking, name='booking'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('records/', views.records, name='records'),

    path('customers/', views.customers, name='customers'),

    path(
        'delete-booking/<int:id>/',
        views.delete_booking,
        name='delete_booking'
    ),

    path('login/', views.admin_login, name='login'),

    path('logout/', views.admin_logout, name='logout'),

]