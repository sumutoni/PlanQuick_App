from django.views.generic import TemplateView
from .forms import UploadForm
from django.shortcuts import render
from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = 'home.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
     template_name = 'contacts.html'

class ProfilePageView(TemplateView):
      template_name = 'profile.html'


def UploadView(request):
    form = None
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        file = request.FILES['file']
        return HttpResponse("The uploaded form is " + str(file))
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form':form})
