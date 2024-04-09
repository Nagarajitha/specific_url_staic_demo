from django.shortcuts import render

# Create your views here.
def veg(request):
    return render(request,'veg.html')

def nonveg(request):
    return render(request,'nonveg.html')


