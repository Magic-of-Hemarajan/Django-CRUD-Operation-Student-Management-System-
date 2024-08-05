from django.shortcuts import render,redirect, get_object_or_404
from . forms import StudentForms
from . models import StudentModels

# Create your views here.
def index(request):
    if request.method == 'POST':
        form=StudentForms(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('read')
    else:
        form=StudentForms()
    title = "Create Student"
    student="Create Details"
    context ={
        'title': title,
        'form': form,
        'student' : student,
    }
    return render(request,'student.html', context)

def read(request):
    details =StudentModels.objects.all()
    context ={
        'details':details,
    }

    return render(request,'read.html',context)

def student_deleted(request, id):
    student = StudentModels.objects.get(id=id)
    student.delete()
    return redirect('read')

def student_update(request, id):
    task = get_object_or_404(StudentModels, id=id)
    if request.method == 'POST':
        form = StudentForms(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = StudentForms(instance=task)
    
    student = "UPDATE Detials"
    context={
        'form':form,
        'student':student,
    }
    return render(request, 'update.html', context)