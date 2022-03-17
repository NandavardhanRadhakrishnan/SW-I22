from django.shortcuts import render
from .models import Job_seeker

# Create your views here.


def index(request):
    return render(request, 'apply_job/index.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        DOB = request.POST['DOB']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        qualification = request.POST['qualification']

        new_job_seeker = Job_seeker(name=name, DOB=DOB, email=email, contact=contact, password=password, qualification=qualification)
        new_job_seeker.save()

    return render(request, 'apply_job/register.html')


def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')

    emails=Job_seeker.objects.values_list('email',flat=True)
    print(emails)

    if email in emails:
        if password==Job_seeker.objects.get(email=email).password:
            return logged_in(request, email)
        else:
            return render(request, 'apply_job/login.html',{'error':'Incorrect password'})
    else:
        return render(request, 'apply_job/login.html',{'error':'Incorrect email'})

def logged_in(request, email):
    profile=list(Job_seeker.objects.filter(email=email))[0]
    print(profile)
    print(profile.qualification)
    # TODO convert qualification to parsable format and get all elibible jobs from employee list
    
    return render(request, 'apply_job/victory.html',{'email':email})

