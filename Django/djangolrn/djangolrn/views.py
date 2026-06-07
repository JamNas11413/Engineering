# from django.http import HttpResponse
from django.shortcuts import render


# def homepage(request):
#     return HttpResponse("hello world, i am home.")

# def about(req):
#     return HttpResponse("it is an about page")

# def contact(req):
#     return HttpResponse("it is a contact page")


def homepage(request):
    # we can:   
        # pull data from a db
        # fransform data
        # send emails 
        # etc
    return render(request, "home.html") 

def about(req):
    # req.user  # the rquest has an attribute and it is rhe job of the uthentication middleware 
    return render(req, "about.html", {'name': 'jamal'}) # dynamic value as dictionary 

def contact(req):
    return render(req, "contact.html")      # by hovering over the name of the func we can see it sdefiettion; so renderreturn an http responce  