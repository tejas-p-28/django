from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1': 'this is sent',
        'variable2' : 'this is variable 2'
    }
    return render(request,'index.html',context)
    # return HttpResponse('This is homepage')

def about(request):
    return HttpResponse('This is aboutpage')

def services(request):
    return HttpResponse('This is services page')

def contact(request):
    return HttpResponse('This is contact page')