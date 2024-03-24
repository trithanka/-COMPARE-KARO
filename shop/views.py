

from django.http import HttpResponse
from .models import Product

def index(request):
    return HttpResponse("Index Shop")
