from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from.views import dashboard

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login')
]