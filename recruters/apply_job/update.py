from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
# import django
# django.setup()

from .models import College, Staff

retiring_age=65
threshold_months=6

def update_job():
    print('iegneg')
    for college in College.objects.all():
        retiring_prof=[]
        for staff in Staff.objects.filter(college_name=college):
            if staff.DOB.year < datetime.now().year - retiring_age-datetime(month=threshold_months):
                retiring_prof.append(staff)
        
        # TODO send email to college

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_job(func=update_job,trigger='cron',year='*',month='*',day='last')
    # scheduler.add_job(func=update_job,trigger='interval',seconds=10)
    scheduler.start()