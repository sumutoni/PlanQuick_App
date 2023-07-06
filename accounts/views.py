from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfilePageView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('dashboard')
    template_name = 'dashboard/profile.html'

    def get_object(self):
        return self.request.user