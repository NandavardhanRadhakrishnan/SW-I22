from django.shortcuts import render
from .models import Job_seeker, Staff
from . import parse_qualification
import datetime
import dateutil

retiring_age = 65
threshold_months = 6

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
        qualification_unformatted = request.POST['qualification']
        qualification = parse_qualification.parse_qualification(qualification_unformatted)

        new_job_seeker = Job_seeker(name=name, DOB=DOB, email=email, contact=contact, password=password, qualification=qualification)
        new_job_seeker.save()

    return render(request, 'apply_job/register.html')


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    emails = Job_seeker.objects.values_list('email', flat=True)
    print(emails)

    if email in emails:
        if password == Job_seeker.objects.get(email=email).password:
            return logged_in(request, email)
        else:
            return render(request, 'apply_job/login.html', {'error': 'Incorrect password'})
    else:
        return render(request, 'apply_job/login.html', {'error': 'Incorrect email'})


def logged_in(request, email):
    profile = list(Job_seeker.objects.filter(email=email))[0]
    # print(profile)
    # print(profile.qualification)

    context = {'vacancies': eligible_vacancies(request, vacancies(request), profile)}

    return render(request, 'apply_job/victory.html', {'email': email})


def vacancies(request):
    staffs = Staff.objects.all()
    retiring_staff = []
    for staff in staffs:
        if dateutil.relativedelta.relativedelta(datetime.datetime.now(), staff.DOB).years >= retiring_age-datetime.datetime(month=threshold_months):
            retiring_staff.append(staff)

    return retiring_staff


def eligible_vacancies(request, vacancies, profile):
    eligible_vac = []
    for vacancy in vacancies:
        for qualification in profile.qualification:
            if qualification[0] >= vacancy.qualification[0] and qualification[1] == vacancy.qualification[1]:
                eligible_vac.append(vacancy)

    return eligible_vac
