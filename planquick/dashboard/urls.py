from django.urls import path
from .views import HomePageView, DashboardView, AboutPageView, ContactPageView, ChartPageView, StatPageView, UploadView, DeleteUpload
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardView, name='dashboard'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('dashboard/upload/', UploadView, name='upload'),
    path('dashboard/delete/', DeleteUpload, name='delete'),
    path('dashboard/charts/', ChartPageView, name='charts'),
    path('dashboard/statements/', StatPageView, name='statements'),
]
