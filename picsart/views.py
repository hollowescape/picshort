from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(" hello")
def PrivacyPolicy(request):
    return render(request,'index.html')
def TermsConditions(request):
    return render(request, 'Terms.html')
    