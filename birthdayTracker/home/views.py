from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        # return HttpResponse('Hello, this is home view')

    return render(request, 'home/index.html')