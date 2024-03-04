from django.conf.urls.static import static
from django.urls import path

from travel import settings
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>/', views.ProfileUpdate.as_view(), name='profile'),
]+static(settings.MEDIA_URL, document_root=settings)