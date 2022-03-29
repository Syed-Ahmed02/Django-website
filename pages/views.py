from django.http import HttpResponse
from django.shortcuts import render

def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user) #prints the user 
    return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
    return render(request,"contact.html",{}) #String of html code (not actually html)

def about_view(request,*args,**kwargs):
    my_context = { 
        "my_text" : "this is about me",
        "my_number" : 123,
        "my_list" : [123,4242,12313]

    }
    return render(request,"about.html",my_context)