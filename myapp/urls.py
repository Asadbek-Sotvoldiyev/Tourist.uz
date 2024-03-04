from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('packages/', views.packages, name='packages'),
    path('contact/', views.contact, name='contact'),
    path('showcat/<int:id>/', views.show_cat, name='show_cat'),
    path('about_pack/<int:pk>/', views.aboutView.as_view(), name='about_pack'),
]