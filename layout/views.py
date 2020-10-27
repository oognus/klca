from django.shortcuts import render

from .models import Home

# Create your views here.
def index(request):

    homes = Home.objects.all().first()
    print(homes)
	
    context = {
        'title': homes.title
    }

    return render(request, 'layout/index.html', context)