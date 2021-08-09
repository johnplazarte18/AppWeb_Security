from django.shortcuts import render,HttpResponse

# Create your views here.
def vwIndex(request):
    return render(request, "index.html")


