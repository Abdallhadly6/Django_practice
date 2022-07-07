from django.shortcuts import render
from django.http import HttpRequest, HttpResponse , HttpResponseRedirect
from . models import Student , Track
from .forms import StudentForm , TrackForm
# Create your views here.

def getStudent (request , st_id):
    st = Student.objects.get(id = st_id)
    context = {'st' : st}
    return render(request , 'opensource/student_details.html' , context)

def getAllStudents (request):
    all_stedents = Student.objects.all()
    context = {'students' : all_stedents}
    return render(request , 'opensource/students.html' , context)

def newStudent(request):
    if request.method=="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/opensource/all')
        
    else:
        form = StudentForm()
    context = {'form' : form}
    return render(request , 'opensource/new_student.html' , context)

def editStudent(request , st_id):
    st = Student.objects.get(id = st_id)
    st_form = StudentForm(instance=st)  # fully with data of student
    if request.method=="POST":
        st_form = StudentForm(request.POST , instance=st)
        if st_form.is_valid():
            st_form.save()
            return HttpResponseRedirect('/opensource/all')
    context = {'form' : st_form}
    return render(request , 'opensource/new_student.html' , context)

def deleteStudent (request , st_id):
    st = Student.objects.get(id = st_id)
    st.delete()
    return HttpResponseRedirect('/opensource/all')

