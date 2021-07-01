from django.shortcuts import redirect, render
from django.http import HttpResponse
from root.models import Url

def getQuery(req):
    if req.method =="POST":
        full_url=req.POST.get("full_url")
        obj = Url.create(full_url)
        return render(req, 'root/index.html',{
            "full_url":obj.full_url,
            "short_url":req.get_host()+'/'+obj.short_url
        })

    return render(req, 'root/index.html')
    
def routeToUrl(req, key):
    try:
        obj=Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        return redirect(getQuery)
    
    # return redirect(req,'root/index.html')
    

# Create your views here.
