import datetime as dt
from enum import Enum



def date_time():
    prompts = {
        "month": None,
        "day": None,
        "year": None,
        "hour": None,
        "minute": None,
        "ampm": None
    }

    for key in prompts:
        prompts[key] = input(f"{key}: ")

    filled = f"{prompts['month']} {prompts['day']}, {prompts['year']} " \
             f"{prompts['hour']}:{prompts['minute']} {prompts['ampm']}"
    print(filled)

    # filled = 'Jul 10, 1999 10:10 AM'
    birth_dt = dt.datetime.strptime(filled, "%b %d, %Y %I:%M %p")
    age_delta = dt.datetime.now() - birth_dt

    days = age_delta.days
    hours = age_delta.seconds // 3600
    minutes = age_delta.seconds % 60
    seconds = age_delta.total_seconds()
    
    print(f'It has been {days} days, {hours} hours,{minutes} minutes, and {seconds} seconds since then.')