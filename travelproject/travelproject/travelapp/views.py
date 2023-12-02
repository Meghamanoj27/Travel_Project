from django.shortcuts import render
from .models import place, workers


# Create your views here.
def index(request):
    obj=place.objects.all()
    obj2=workers.objects.all()
    return render(request,'index.html',{'result':obj, "result2":obj2})

