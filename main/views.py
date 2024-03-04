from django.shortcuts import render
from main.models import Slide , Customer
from service.models import Service 
from project.models import Project
from shop.models import Product
from blog.models import Blog


def home (request):
    
    slider = Slide.objects.all()
    services = Service.objects.all().order_by("-views")[:6]
    customers = Customer.objects.all()
    projects = Project.objects.all().order_by("order_number")
    products = Product.objects.all().order_by("-views")[:3]
    blogs = Blog.objects.all().order_by("-views")[:3]
    
    context = {
        'slider':slider,
        'services':services,
        'customers':customers,
        'projects':projects,
        'products':products,
        'blogs':blogs,
        
    }
    
    return render(request, 'home.html',context)

