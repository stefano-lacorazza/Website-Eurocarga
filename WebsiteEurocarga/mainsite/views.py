from django.shortcuts import render

def index(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/index.html', context)

def about(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/about.html', context)