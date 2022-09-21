from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  render
from datetime import datetime

# Create your views here.
# def home(request):
#     return HttpResponse("Hello, Tryggve")

def home(request):
    return render(
        request,
        'tryggve/index.html',
        {
            'name': "arvid",
            'date': datetime.now()
        }
    )
