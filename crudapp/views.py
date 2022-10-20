from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def std_db(request):
    return render(request, 'std_db.html', {
        
    })
