from django.shortcuts import render,redirect

from MyApp.models import Student
# Create your views here.

def Welcome(request):
    return render(request,'Welcome.html')


def Register(request):
    if request.method == "POST":
        fname = request.POST.get('fullname')
        mobile = request.POST.get('mobile')
        course = request.POST.get('course')
        email = request.POST.get('email')
        password=request.POST.get('password')
        
        std=Student(Name=fname,Mobile=mobile,Course=course,Email=email,Password=password)
        std.save()
        return redirect('Infromation')
        
    return render(request,'registration.html')


def Infromation(request):
    std=Student.objects.all()
    context={
        'std':std
    }
    return render(request,'Infromation.html',context)


def login(request):
    return render(request,'login.html')


def Courses(request):
    return render(request,'Courses.html')