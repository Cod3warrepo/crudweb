from django.shortcuts import redirect, render
from .models import StudentDB
from .forms import StdForm


def index(request):
    return render(request, 'index.html')

def std_db(request):
    studentdb = StudentDB.objects.all()
    return render(request, 'std_db.html', {
        'studentdb': studentdb
        
    })

def std_db_add(request):
    stdform = StdForm()
    return render(request, 'std_db_add.html', {
        'stdform': stdform
        
    })

def std_db_add_func(request):
    stdform = StdForm(request.POST)
    stdform.save()
    return redirect('std_db')

def std_db_edit(request, id):
    studentdb = StudentDB.objects.get(id=id)
    return render(request, 'std_db_edit.html', {
        'studentdb': studentdb
        
    })

def std_db_edit_func(request, id):
    studentdb = StudentDB.objects.get(id=id)
    stdform = StdForm(request.POST, instance=studentdb)
    stdform.save()
    return redirect('std_db')



def std_db_delete(request, id):
    studentdb = StudentDB.objects.get(id=id)
    studentdb.delete()
    return redirect('std_db')
