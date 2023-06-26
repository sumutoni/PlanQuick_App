from django.urls import path
from .views import HomePageView, DashboardView, AboutPageView, ContactPageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
]
