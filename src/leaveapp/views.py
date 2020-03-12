from django.shortcuts import render
from django.http import HttpResponse
# from django.template import index

# Create your views here.
def Signin(request):
    template_name = 'index.html'
    return render(request, template_name, { 'username' : 'Leave Application Form'})

def Apply(request):
    template_name = 'test.html'
    return render(request, template_name, {})
