from django.shortcuts import render
from etc.models import Faq

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def survey(request):
    return render(request,'survey.html')

def search(request):
    return render(request,'search.html')

def error_404_view(request, exception):
    return render(request,'404.html')

def faq(request):
    soalha = Faq.objects.all() 
    context= {
        'soalaat':soalha,
    }
    return render(request,'faq.html',context)