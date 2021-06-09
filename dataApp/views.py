from django.shortcuts import render
from django.http import HttpResponse
from dataApp.models import Student

# Create your views here.

def display_db(request):
    myName = "Paul"
    stud_data = Student.objects.all()
    display_data = {'name':myName , 'stud_list':stud_data}
    return render(request,'myData.html' , context = display_data)
