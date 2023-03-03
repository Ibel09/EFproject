import csv

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum

from rest_framework.response import Response
from .serializers import FundSerializer
from .models import Fund

# new
from rest_framework import viewsets

def index(request):
    strategy = request.GET.get('strategy')
   
    if strategy == 'None' or strategy == None:
        fund_results = Fund.objects.all()
       
    else:
        fund_results = Fund.objects.filter(strategy=strategy) 
    
    context = {
        'fundResults': fund_results,
        'fundCount': fund_results.count(),
        'aumSum': Fund.objects.exclude(aum__isnull=True).aggregate(Sum('aum'))['aum__sum']
    }
    
    return render(request, 'fundsapp/index.html', context)


def upload_funds(request):
    Fund.objects.all().delete()
    # to refresh the db before uploading to show uploading functionality works

    file = request.FILES["csv_file"]
    file_data = file.read().decode('utf-8-sig').splitlines()
    rows = list(csv.DictReader(file_data, delimiter=","))
    
    for counter, row in enumerate(rows):
        f = Fund()
        f.name = row['Name']
        f.strategy = row['Strategy']
        if row['AUM (USD)']:
            f.aum = row['AUM (USD)']
        if row['Inception Date']:
            f.inception_date = row['Inception Date']
        f.save()
    return HttpResponse("File uploaded successfully.")


class FundViewSet(viewsets.ModelViewSet):

   serializer_class = FundSerializer

   def get_queryset(self):
    
        queryset = Fund.objects.all()
        strategy = self.request.query_params.get('strategy')
        if strategy != None:
            queryset = queryset.filter(strategy=strategy)
        return queryset   