from django.shortcuts import render
from .models import Ring

# Create your views here.
def home(request):
    context = {
        'rings': Ring.objects.all()
    }
    return render(request, 'rings/home.html', context)
