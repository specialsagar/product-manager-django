from django.shortcuts import render
from django.http import HttpResponse
from .models import Company, Invoice, Order, Product


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_companies(request):
    company_list = Company.objects.all()
    return HttpResponse(company_list)

def post_companies(request):
    received_json_data=json.loads(request.body)
    new_company = Company.objects.create(**received_json_data)
    return HttpResponse()

def get_products(request):
    