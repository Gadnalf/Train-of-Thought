from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def thought(request):
    return render(request, 'index.html', {})