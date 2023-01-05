from django.shortcuts import render

# Create your views here.
def static1(request):
    return render(request,'static1.html')
