from django.shortcuts import render
from django.http import HttpResponse
from web_site.models import Pdfs,model_QA
from web_site.forms import ContactForm


def index(request):
    return render(request,"index.html")

def pdf(request):
    data=Pdfs.objects.order_by('subject')
    print(data)
    return render(request,"pdf.html",{"data":data})

def model_Q(request):
    data=model_QA.objects.order_by('subject')

    return render(request,"model.html",{"data":data})

def con(request):
    form = ContactForm()
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data (e.g., save to DB or send email)
            # For now, we just print and set success to True
            print(form.cleaned_data['name'])
            success = True
            form = ContactForm()  # Reset the form after success
            
    return render(request, "contact.html", {"form": form, "success": success})

# Create your views here.
