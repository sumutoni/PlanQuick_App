#!/usr/bin/python3
import json
import datetime
import re
import sqlite3

def momo_data():
    for item in data:
        dict1 = {}
        dict1['filter'] = item.get('body')

        for i in dict1.values():
            dct = {}

            #add data creation date
            dct['created_at'] = datetime.datetime.today().strftime('%Y-%m-%d')


            # this is to filter transaction id for mpesa i'll replace with momo
            """
            if i.find("Failed") > -1:
                continue
            else:
                dct['ref_id'] = re.sub("confirmed.*|Confirmed.*", "",i)
            try:
                dct['ref_id'] = re.sub("confirmed.*|Confirmed.*", "",i)
            except:
                re.search("Failed|Insufficient funds|insufficient funds", i)
                continue
            """

            # filter transaction type
            if i.find("to Bundles" or "to Data") >-1:
                dct['type'] = "Airtime & Bundle"
            elif i.find("have received") > -1:
                dct['type'] = "Received"
            elif i.find("transferred to") > -1:
                dct['type'] = "Customer Transfer"
            elif i.find("withdrawn") > -1:
                dct['type'] = "Withdraw"
            elif i.find("paid to") > -1:
                dct['type'] = "Merchant Payment"
            elif i.find("Insufficient funds") > -1:
                continue
            elif i.find("insufficient funds") > -1:
                continue
            elif i.find("Failed.*") > -1:
                continue
            else:
                dct['type'] = "Customer Transfer"


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


