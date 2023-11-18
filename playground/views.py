from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculate():
    x,y = 1,2
    return x
#req handler
def say_hello(request):
    # return HttpResponse('Hello world')
    x = calculate()
    y=2
    return render(request, 'hello.html',{'name':'moshe'})