from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
     template_name = 'contacts.html'
