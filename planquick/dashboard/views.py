from typing import Self
from django.views.generic import TemplateView
from .forms import UploadForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Transactions
import json
import datetime
import re


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
        if form.is_valid():
            file = request.FILES['file']
            result = []
            data = json.load(file)

        """
        Filters transactions
        """
        for item in data:
            dict1 = {}
            dict1['filter'] = item.get('body')

            for i in dict1.values():
                dct = {}

                # Append upload date
                dct['created_at'] = datetime.datetime.today().strftime('%Y-%m-%d')
                
                # Retrieve unique ref id
                if re.search("Failed", i):
                    continue
                else:
                    dct['ref_id'] = re.sub("confirmed.*|Confirmed.*", "",i)

                # Categorize transactions
                if re.search("sent to SAFARICOM", i):
                    dct['trn_type'] = "Airtime & Bundle"
                elif re.search("Give", i):
                    dct['trn_type'] = "Deposit"
                elif re.search("sent to", i):
                    dct['trn_type'] = "Customer Transfer"
                elif re.search("transferred to", i):
                    dct['trn_type'] = "Transfer"
                elif re.search("withdraw", i):
                    dct['trn_type'] = "Withdrawal"
                elif re.search("for account", i):
                    dct['trn_type'] = "Pay Bill"
                elif re.search("paid to", i):
                    dct['trn_type'] = "Merchant Payment"
                elif re.search("Insufficient funds", i):
                    continue
                elif re.search("insufficient funds", i):
                    continue
                elif re.search("Failed.*", i):
                    continue
                else:
                    dct['trn_type'] = "Recieved"
                
                # Retrieve transaction amount
                ns = re.sub(",", "", i)
                amt = re.search(r'(?<=Ksh)\w+', ns)
                try:
                    amt = amt.group(0)
                    amt = int(float(amt))
                except:
                    pass
                dct['amount'] = amt

                # Retrieve transaction date
                try:
                    day = re.search(r"\d+/\d+/\d+", i)
                    day = day.group(0)
                    day = day.replace("/","-")
                    date = datetime.datetime.strptime(day, '%d-%m-%y').date()
                    dct['trn_date'] = datetime.datetime.strptime(day, '%d-%m-%y').date()
                except:
                    pass
                result.append(dct)
        
        # Delete entries
        Transactions.objects.all().delete()
        """
        # Save entries
        for mydict in result:
            Transactions.owner = request.user.email
            c, new = Transactions.objects.filter(owner=request.user.email).get_or_create(**mydict)
            #c, new = Transactions.objects.get_or_create(**mydict)
            if new:
                Transactions.save(c)    
        """
        messages.add_message(request, messages.SUCCESS, "Success!")
        return redirect('/dashboard/')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form':form})