from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#  Create the endpoints here (Location of the server)
def main(request):
    return HttpResponse("Hello")
