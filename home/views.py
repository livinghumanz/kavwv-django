from django.shortcuts import render

# Create your views here.
def homeIndex(request):
    return render(request,'home/index.html')