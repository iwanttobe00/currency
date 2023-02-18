from django.shortcuts import render
import requests

app_name = 'valuta'

def currency(request):
    response = requests.get(url='https://api.exchangerate.host/latest').json()
    currencies = response.get('rates')

    if request.method == 'GET':
        context = {
            'currencies': currencies,
        }
        return render(request, 'index.html', context)

    if request.method == 'POST':
        from_amount = float(request.POST.get('from_amount'))
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')
        converted_amount = round((currencies[to_curr]) / currencies[from_curr] * float(from_amount), 2)
        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount,
            'currencies': currencies,
            'converted_amount': converted_amount,
        }
        return render(request, 'index.html', context)
