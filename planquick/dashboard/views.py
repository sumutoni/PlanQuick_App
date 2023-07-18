from django.views.generic import TemplateView, DeleteView
from django.db.models import Sum
from .forms import UploadForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from .models import Transactions
import json
import datetime
import re


class HomePageView(TemplateView):
    template_name = 'home.html'

def DashboardView(request):

    amt_sent = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').aggregate(Sum('amount'))['amount__sum']
    amt_received = Transactions.objects.filter(owner=request.user.email, trn_type='Received').aggregate(Sum('amount'))['amount__sum']
    amt_withdrawn = Transactions.objects.filter(owner=request.user.email, trn_type='Withdrawal').aggregate(Sum('amount'))['amount__sum']
    amt_bundle = Transactions.objects.filter(owner=request.user.email, trn_type='Airtime & Bundle').aggregate(Sum('amount'))['amount__sum']
    amt_deposited = Transactions.objects.filter(owner=request.user.email, trn_type='Deposit').aggregate(Sum('amount'))['amount__sum']
    amt_paybill = Transactions.objects.filter(owner=request.user.email, trn_type='Pay Bill').aggregate(Sum('amount'))['amount__sum']
    amt_merchant = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').aggregate(Sum('amount'))['amount__sum']
    transacted = Transactions.objects.filter(owner=request.user.email).aggregate(Sum('amount'))['amount__sum']

    #all year merchant transfer
    Merchant_jan = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='1').aggregate(Sum('amount'))['amount__sum']
    Merchant_feb = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='2').aggregate(Sum('amount'))['amount__sum']
    Merchant_mar = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='3').aggregate(Sum('amount'))['amount__sum']
    Merchant_apr = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='4').aggregate(Sum('amount'))['amount__sum']
    Merchant_may = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='5').aggregate(Sum('amount'))['amount__sum']
    Merchant_jun = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='6').aggregate(Sum('amount'))['amount__sum']
    Merchant_jul = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='7').aggregate(Sum('amount'))['amount__sum']
    Merchant_aug = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='8').aggregate(Sum('amount'))['amount__sum']
    Merchant_sep = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='9').aggregate(Sum('amount'))['amount__sum']
    Merchant_oct = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='10').aggregate(Sum('amount'))['amount__sum']
    Merchant_nov = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='11').aggregate(Sum('amount'))['amount__sum']
    Merchant_dec = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='12').aggregate(Sum('amount'))['amount__sum']

    #all year received
    Received_jan = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='1').aggregate(Sum('amount'))['amount__sum']
    Received_feb = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='2').aggregate(Sum('amount'))['amount__sum']
    Received_mar = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='3').aggregate(Sum('amount'))['amount__sum']
    Received_apr = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='4').aggregate(Sum('amount'))['amount__sum']
    Received_may = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='5').aggregate(Sum('amount'))['amount__sum']
    Received_jun = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='6').aggregate(Sum('amount'))['amount__sum']
    Received_jul = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='7').aggregate(Sum('amount'))['amount__sum']
    Received_aug = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='8').aggregate(Sum('amount'))['amount__sum']
    Received_sep = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='9').aggregate(Sum('amount'))['amount__sum']
    Received_oct = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='10').aggregate(Sum('amount'))['amount__sum']
    Received_nov = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='11').aggregate(Sum('amount'))['amount__sum']
    Received_dec = Transactions.objects.filter(owner=request.user.email, trn_type='Recevied').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='12').aggregate(Sum('amount'))['amount__sum']

    #all year sent
    Sent_jan = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='1').aggregate(Sum('amount'))['amount__sum']
    Sent_feb = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='2').aggregate(Sum('amount'))['amount__sum']
    Sent_mar = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='3').aggregate(Sum('amount'))['amount__sum']
    Sent_apr = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='4').aggregate(Sum('amount'))['amount__sum']
    Sent_may = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='5').aggregate(Sum('amount'))['amount__sum']
    Sent_jun = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='6').aggregate(Sum('amount'))['amount__sum']
    Sent_jul = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='7').aggregate(Sum('amount'))['amount__sum']
    Sent_aug = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='8').aggregate(Sum('amount'))['amount__sum']
    Sent_sep = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='9').aggregate(Sum('amount'))['amount__sum']
    Sent_oct = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='10').aggregate(Sum('amount'))['amount__sum']
    Sent_nov = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='11').aggregate(Sum('amount'))['amount__sum']
    Sent_dec = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='12').aggregate(Sum('amount'))['amount__sum']


    test = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='5').aggregate(Sum('amount'))['amount__sum']


    context = {}
    context['transacted'] = transacted or ''
    context['amt_sent'] = amt_sent or ''
    context['amt_received'] = amt_received or ''
    context['amt_bundle'] = amt_bundle or ''
    context['amt_withdrawn'] = amt_withdrawn or ''
    context['amt_deposited'] = amt_deposited or ''
    context['amt_paybill'] = amt_paybill or ''
    context['amt_merchant'] = amt_merchant or ''
    context['test'] = test or ''

    #column graph data context
    context['Merchant_jan'] = Merchant_jan or ''
    context['Merchant_feb'] = Merchant_feb or ''
    context['Merchant_mar'] = Merchant_mar or ''
    context['Merchant_apr'] = Merchant_apr or ''
    context['Merchant_may'] = Merchant_may or ''
    context['Merchant_jun'] = Merchant_jun or ''
    context['Merchant_jul'] = Merchant_jul or ''
    context['Merchant_aug'] = Merchant_aug or ''
    context['Merchant_sep'] = Merchant_sep or ''
    context['Merchant_oct'] = Merchant_oct or ''
    context['Merchant_nov'] = Merchant_nov or ''
    context['Merchant_dec'] = Merchant_dec or ''

    context['Received_jan'] = Received_jan or ''
    context['Received_feb'] = Received_feb or ''
    context['Received_mar'] = Received_mar or ''
    context['Received_apr'] = Received_apr or ''
    context['Received_may'] = Received_may or ''
    context['Received_jun'] = Received_jun or ''
    context['Received_jul'] = Received_jul or ''
    context['Received_aug'] = Received_aug or ''
    context['Received_sep'] = Received_sep or ''
    context['Received_oct'] = Received_oct or ''
    context['Received_nov'] = Received_nov or ''
    context['Received_dec'] = Received_dec or ''


    context['Sent_jan'] = Sent_jan or ''
    context['Sent_feb'] = Sent_feb or ''
    context['Sent_mar'] = Sent_mar or ''
    context['Sent_apr'] = Sent_apr or ''
    context['Sent_may'] = Sent_may or ''
    context['Sent_jun'] = Sent_jun or ''
    context['Sent_jul'] = Sent_jul or ''
    context['Sent_aug'] = Sent_aug or ''
    context['Sent_sep'] = Sent_sep or ''
    context['Sent_oct'] = Sent_oct or ''
    context['Sent_nov'] = Sent_nov or ''
    context['Sent_dec'] = Sent_dec or ''


    return render(request, 'dashboard.html', context)

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
     template_name = 'contacts.html'

def ChartPageView(request):
    # Retrieve transactions from sqlite and filter by type
    amt_sent = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').aggregate(Sum('amount'))['amount__sum']
    amt_received = Transactions.objects.filter(owner=request.user.email, trn_type='Received').aggregate(Sum('amount'))['amount__sum']
    amt_withdrawn = Transactions.objects.filter(owner=request.user.email, trn_type='Withdrawal').aggregate(Sum('amount'))['amount__sum']
    amt_bundle = Transactions.objects.filter(owner=request.user.email, trn_type='Airtime & Bundle').aggregate(Sum('amount'))['amount__sum']
    amt_deposited = Transactions.objects.filter(owner=request.user.email, trn_type='Deposit').aggregate(Sum('amount'))['amount__sum']
    amt_paybill = Transactions.objects.filter(owner=request.user.email, trn_type='Pay Bill').aggregate(Sum('amount'))['amount__sum']
    amt_merchant = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').aggregate(Sum('amount'))['amount__sum']
    transactions = Transactions.objects.all().order_by('trn_type')

    #all year merchant transfer
    Merchant_jan = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='1').aggregate(Sum('amount'))['amount__sum']
    Merchant_feb = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='2').aggregate(Sum('amount'))['amount__sum']
    Merchant_mar = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='3').aggregate(Sum('amount'))['amount__sum']
    Merchant_apr = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='4').aggregate(Sum('amount'))['amount__sum']
    Merchant_may = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='5').aggregate(Sum('amount'))['amount__sum']
    Merchant_jun = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='6').aggregate(Sum('amount'))['amount__sum']
    Merchant_jun = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='6').aggregate(Sum('amount'))['amount__sum']
    Merchant_jun = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='6').aggregate(Sum('amount'))['amount__sum']
    Merchant_jul = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='7').aggregate(Sum('amount'))['amount__sum']
    Merchant_aug = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='8').aggregate(Sum('amount'))['amount__sum']
    Merchant_sep = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='9').aggregate(Sum('amount'))['amount__sum']
    Merchant_oct = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='10').aggregate(Sum('amount'))['amount__sum']
    Merchant_nov = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='11').aggregate(Sum('amount'))['amount__sum']
    Merchant_dec = Transactions.objects.filter(owner=request.user.email, trn_type='Merchant Payment').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='12').aggregate(Sum('amount'))['amount__sum']

    #all year received
    Received_jan = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='1').aggregate(Sum('amount'))['amount__sum']
    Received_feb = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='2').aggregate(Sum('amount'))['amount__sum']
    Received_mar = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='3').aggregate(Sum('amount'))['amount__sum']
    Received_apr = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='4').aggregate(Sum('amount'))['amount__sum']
    Received_may = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='5').aggregate(Sum('amount'))['amount__sum']
    Received_jun = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='6').aggregate(Sum('amount'))['amount__sum']
    Received_jul = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='7').aggregate(Sum('amount'))['amount__sum']
    Received_aug = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='8').aggregate(Sum('amount'))['amount__sum']
    Received_sep = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='9').aggregate(Sum('amount'))['amount__sum']
    Received_oct = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='10').aggregate(Sum('amount'))['amount__sum']
    Received_nov = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='11').aggregate(Sum('amount'))['amount__sum']
    Received_dec = Transactions.objects.filter(owner=request.user.email, trn_type='Received').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='12').aggregate(Sum('amount'))['amount__sum']

    #all year sent
    Sent_jan = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='1').aggregate(Sum('amount'))['amount__sum']
    Sent_feb = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='2').aggregate(Sum('amount'))['amount__sum']
    Sent_mar = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='3').aggregate(Sum('amount'))['amount__sum']
    Sent_apr = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='4').aggregate(Sum('amount'))['amount__sum']
    Sent_may = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='5').aggregate(Sum('amount'))['amount__sum']
    Sent_jun = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='6').aggregate(Sum('amount'))['amount__sum']
    Sent_jul = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='7').aggregate(Sum('amount'))['amount__sum']
    Sent_aug = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='8').aggregate(Sum('amount'))['amount__sum']
    Sent_sep = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='9').aggregate(Sum('amount'))['amount__sum']
    Sent_oct = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='10').aggregate(Sum('amount'))['amount__sum']
    Sent_nov = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='11').aggregate(Sum('amount'))['amount__sum']
    Sent_dec = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='12').aggregate(Sum('amount'))['amount__sum']


    test = Transactions.objects.filter(owner=request.user.email, trn_type='Customer Transfer').filter(trn_date__year=datetime.datetime.today().year).filter(trn_date__month='5').aggregate(Sum('amount'))['amount__sum']




    #column graph data context
    context = {}
    context['Merchant_jan'] = Merchant_jan or ''
    context['Merchant_feb'] = Merchant_feb or ''
    context['Merchant_mar'] = Merchant_mar or ''
    context['Merchant_apr'] = Merchant_apr or ''
    context['Merchant_may'] = Merchant_may or ''
    context['Merchant_jun'] = Merchant_jun or ''
    context['Merchant_jul'] = Merchant_jul or ''
    context['Merchant_aug'] = Merchant_aug or ''
    context['Merchant_sep'] = Merchant_sep or ''
    context['Merchant_oct'] = Merchant_oct or ''
    context['Merchant_nov'] = Merchant_nov or ''
    context['Merchant_dec'] = Merchant_dec or ''

    context['Received_jan'] = Received_jan or ''
    context['Received_feb'] = Received_feb or ''
    context['Received_mar'] = Received_mar or ''
    context['Received_apr'] = Received_apr or ''
    context['Received_may'] = Received_may or ''
    context['Received_jun'] = Received_jun or ''
    context['Received_jul'] = Received_jul or ''
    context['Received_aug'] = Received_aug or ''
    context['Received_sep'] = Received_sep or ''
    context['Received_oct'] = Received_oct or ''
    context['Received_nov'] = Received_nov or ''
    context['Received_dec'] = Received_dec or ''


    context['Sent_jan'] = Sent_jan or ''
    context['Sent_feb'] = Sent_feb or ''
    context['Sent_mar'] = Sent_mar or ''
    context['Sent_apr'] = Sent_apr or ''
    context['Sent_may'] = Sent_may or ''
    context['Sent_jun'] = Sent_jun or ''
    context['Sent_jul'] = Sent_jul or ''
    context['Sent_aug'] = Sent_aug or ''
    context['Sent_sep'] = Sent_sep or ''
    context['Sent_oct'] = Sent_oct or ''
    context['Sent_nov'] = Sent_nov or ''
    context['Sent_dec'] = Sent_dec or ''


    context['transactions'] = transactions or ''
    context['amt_sent'] = amt_sent or ''
    context['amt_received'] = amt_received or ''
    context['amt_bundle'] = amt_bundle or ''
    context['amt_withdrawn'] = amt_withdrawn or ''
    context['amt_deposited'] = amt_deposited or ''
    context['amt_paybill'] = amt_paybill or ''
    context['amt_merchant'] = amt_merchant or ''


    return render(request,'charts.html', context)


def StatPageView(request):
    # Retrieve all user transactions
    transactions = Transactions.objects.filter(owner=request.user.email).order_by('trn_type')

    context = {}
    context['transactions'] = transactions

    return render(request,'statements.html', context)


def UploadView(request):
    #transaction data upload
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

        # check for mpesa transactions
        if data[0].get('address') == 'MPESA':
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
                    if i.find("sent to SAFARICOM" or "sent to Safaricom") >-1:
                        dct['trn_type'] = "Airtime & Bundle"
                    elif i.find("Give") > -1:
                        dct['trn_type'] = "Deposit"
                    elif i.find("sent to" and "for account") > -1:
                        dct['trn_type'] = "Pay Bill"
                    elif i.find("have received") > -1:
                        dct['trn_type'] = "Received"
                    elif i.find("transferred to") > -1:
                        dct['trn_type'] = "Transfer"
                    elif i.find("Withdraw") > -1:
                        dct['trn_type'] = "Withdraw"
                    elif i.find("paid to") > -1:
                        dct['trn_type'] = "Merchant Payment"
                    elif i.find("Insufficient funds") > -1:
                        continue
                    elif i.find("insufficient funds") > -1:
                        continue
                    elif i.find("Failed.*") > -1:
                        continue
                    else:
                        dct['trn_type'] = "Customer Transfer"

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
                    dct['owner'] = request.user.email
                    result.append(dct)

            #save entries
            for mydict in result:
                try:
                    c, new = Transactions.objects.get_or_create(**mydict)
                except:
                    continue

            print(result)


        # check for momo transactions
        elif data[0].get('address') == 'MOMO':
            for item in data:
                dict1 = {}
                dict1['filter'] = item.get('body')

                for i in dict1.values():
                    dct = {}

                    #add data creation date
                    dct['created_at'] = datetime.datetime.today().strftime('%Y-%m-%d')


                    # Retrieve unique ref id
                    if re.search("Failed", i):
                        continue
                    else:
                        dct['ref_id'] = 'null'

                    # filter transaction type
                    if i.find("to Bundles" or "to Data") >-1:
                        dct['trn_type'] = "Airtime & Bundle"
                    elif i.find("have received") > -1:
                        dct['trn_type'] = "Received"
                    elif i.find("transferred to") > -1:
                        dct['trn_type'] = "Customer Transfer"
                    elif i.find("withdrawn") > -1:
                        dct['trn_type'] = "Withdrawal"
                    elif i.find("Your payment") > -1:
                        dct['trn_type'] = "Merchant Payment"
                    elif i.find("Insufficient funds") > -1:
                        continue
                    elif i.find("insufficient funds") > -1:
                        continue
                    elif i.find("Failed.*") > -1:
                        continue
                    else:
                        dct['trn_type'] = "Customer Transfer"


                    #filter amount
                    ns = re.sub(",", "", i)
                    amt =  re.search(r'\w+(?=\s+RWF)', ns)
                    try:
                        amt = amt.group(0)
                        amt = int(float(amt))
                    except:
                        pass
                    dct['amount'] = amt


                    #filter transaction date
                    try:
                        day = re.search(r'\d{4}-\d{2}-\d{2}', i)
                        day = day.group(0)
                        dct['trn_date'] = datetime.datetime.strptime(day, '%Y-%m-%d').date()
                    except:
                        pass
                    dct['owner'] = request.user.email
                    result.append(dct)

            #save entries
            for mydict in result:
                try:
                    c, new = Transactions.objects.get_or_create(**mydict)
                except:
                    continue
                
            print(result)

        else:
            print('error')

        messages.add_message(request, messages.SUCCESS, "Success!")
        return redirect('/dashboard/')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form':form})


def DeleteUpload(request):
        # delete all user data
        dels = Transactions.objects.filter(owner=request.user.email)
        dels.delete()
        return redirect('/dashboard/')

