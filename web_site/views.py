from django.shortcuts import render
from django.http import HttpResponse
from web_site.models import Pdfs,model_QA


def index(request):
    return render(request,"index.html")

def pdf(request):
    data=Pdfs.objects.order_by('subject')
    print(data)
    return render(request,"pdf.html",{"data":data})

def model_Q(request):
    data=model_QA.objects.order_by('subject')

    return render(request,"model.html",{"data":data})

# Create your views here.
