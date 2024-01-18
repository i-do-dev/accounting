from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chart_of_accounts(request):
    return HttpResponse("This is the chart of accounts page")