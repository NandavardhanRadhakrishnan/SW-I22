from datetime import datetime
from dateutil import relativedelta
import os
from apscheduler.schedulers.background import BackgroundScheduler


# for sending email
from email.mime.message import MIMEMessage
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
from email.mime.text import MIMEText
from django.template.loader import render_to_string

from .models import College, Staff

retiring_age=65
threshold_months=6

def update_job():
    for college in College.objects.all():
        retiring_prof=[]
        for staff in Staff.objects.filter(college_name=college):
            age=relativedelta.relativedelta(datetime.now(),staff.DOB).years
            if age>=retiring_age-threshold_months:
                retiring_prof.append(staff)
            
        notify_college(retiring_prof)

def notify_college(retiring_profs):
    port = 587 
    smtp_server = "smtp.gmail.com"
    college_email=retiring_profs[0].college_name.email
    sender_email="sihtesting9@gmail.com"
    password = "SIHtesting"
    html = render_to_string('apply_job/mail_template.html',{'professors':retiring_profs})

    message=MIMEMultipart("alternative")
    message.attach(MIMEText(html, "html"))
    message['subject'] = "Monthly Report of Retiring Professors"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, college_email, message.as_string())

    

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_job(func=update_job,trigger='cron',year='*',month='*',day='last')
    # scheduler.add_job(func=update_job,trigger='interval',seconds=5)
    scheduler.start()