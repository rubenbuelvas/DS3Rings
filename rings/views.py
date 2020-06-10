from django.shortcuts import render, redirect
from .models import Ring


# Create your views here.
def home(request):
    context = {
        'rings': Ring.objects.all()
    }
    if request.user.is_authenticated:
        return render(request, 'rings/home.html', context)
    else:
        return redirect('users-login')