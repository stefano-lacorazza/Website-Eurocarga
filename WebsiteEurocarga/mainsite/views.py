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

def offices(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/offices.html', context)

def tracking(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/tracker.html', context)


##English sites

def index_en(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/en/index.html', context)

def about_en(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/en/about.html', context)

def team_en(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/en/team.html', context)

def services_en(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/en/services.html', context)

def pqrs_en(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/en/pqr.html', context)

def offices_en(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/en/offices.html', context)