
from django.shortcuts import render

# Create your views here.
def women(request):
    return render(request,'women.html')

def men(request):
    return render(request,'men.html')


