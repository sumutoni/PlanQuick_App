from django.urls import path
from .views import SignupPageView, ProfilePageView
urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('dashboard/profile/', ProfilePageView.as_view(), name='profile'),
]
