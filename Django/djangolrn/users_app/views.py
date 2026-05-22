from django.shortcuts import render

# Create your views here.

def user_lists(request):
    return render(request, 'users_app/user.html', {'name': 'Maryam.'})