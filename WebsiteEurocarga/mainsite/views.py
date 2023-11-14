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

def team(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/team.html', context)

def services(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/services.html', context)

def pqrs(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/pqr.html', context)

def tracking(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/tracker.html', context)