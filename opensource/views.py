from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . models import Student , Track
# Create your views here.

def getStudent (request , st_id):
    st = Student.objects.get(id = st_id)
    return HttpResponse("<h1>Student name : </h1>" + st.fname)

def getAllStudents (request):
    all_stedents = Student.objects.all()
    context = {'students' : all_stedents}
    return render(request , 'opensource/students.html' , context)
