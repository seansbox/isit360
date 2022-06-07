from django.urls import path

from . import views

app_name = 'common'
urlpatterns = [
    path('', views.FrontView.as_view(), name='front'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]