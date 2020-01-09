from django.shortcuts import render
from django.http import HttpResponse
from . models import UserInfo


# Create your views here.
def home(request):

    
    if request.method == 'POST':
        name = request.POST.get("username", False)
        password = request.POST.get("password",False)
        rpassword = request.POST.get("rpassword",False)
        
        if password == rpassword:
                userinfo = UserInfo()
                userinfo.user = name
                userinfo.pwd = password
                userinfo.save()
                
                return render(request, 'home.html', locals())
    
        else:
            return render(request, 'register.html', locals())
        
    else:     
        return render(request, 'home.html',locals())

def success(request):
    
    name = request.POST.get("username", False)
    password = request.POST.get("password",False)
    uu = []
    u = UserInfo.objects.all()

    for i in range(len(u)):
        uu.append(u[i].user)
    
    if name in uu:
            return render(request, 'success.html', locals())
            
    else:
        return render(request, 'homee.html', locals())
        
    

def register(request):
    
    return render(request, 'register.html', locals())