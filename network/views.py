from django.shortcuts import render
from .models import Switch

# Create your views here.
def index(request):
    switches = Switch.objects.all()

    context = {
        'object_list': switches
    }

    return render(request, 'devices/dashboard.html', context)