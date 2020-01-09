from django.shortcuts import render

# Create your views here.
def thought(request):
    return render(request, 'index.html', {})