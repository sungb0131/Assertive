from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login')
    ]