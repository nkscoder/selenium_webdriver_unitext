from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# home_page = None

# this funcation working
# def home_page():
#     pass

def home_page():
    return HttpResponse('<html><title>To-Do lists</title></html>')
