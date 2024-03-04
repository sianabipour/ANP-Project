from django.shortcuts import render
from service.models import Service , RequestedService

def services(request):
    services = Service.objects.all()
    context = {
        'services':services
    }    
    return render(request,'services.html',context)


def single_service(request,slug):
    service = Service.objects.get(slug=slug)
    suggested_services = Service.objects.filter(category=service.category).exclude(slug=slug)[:5]
    msg = None
    msg_type = None
    
    if request.method == 'POST':
        try:
            if not(len(request.POST["phone"]) == 11 and request.POST["phone"][0:2] == "09"):
                msg = "شماره تماس را به صورت صحیح وارد کنید!"
                msg_type = "error"
            else:    
                RequestedService.objects.create(
                    phone = request.POST["phone"],
                    service = service,
                )
                
                msg = "درخواست شما ثبت شد."
                msg_type = "success"

        except:
            msg = "درخواست شما ثبت نشد."
            msg_type = "error"

    context = {
        'service':service,
        'suggested_services':suggested_services,
        'msg':msg,
        'msg_type':msg_type,
    } 
    
    return render(request,'single-service.html',context)