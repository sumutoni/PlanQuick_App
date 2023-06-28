from django.urls import path
from .views import HomePageView, DashboardView, AboutPageView, ContactPageView, ProfilePageView, UploadView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('dashboard/profile/', ProfilePageView.as_view(), name='profile'),
    path('dashboard/upload/', UploadView, name='upload'),
]
