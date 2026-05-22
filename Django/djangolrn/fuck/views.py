from django.shortcuts import render

# Create your views here.
def fuckYou(req):
    return render(req, 'fuck.html')