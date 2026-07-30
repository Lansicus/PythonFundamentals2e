import datetime as dt
from dateutil import parser



def parse_date_or_time(s, mode=None):
    """
    mode: 'date', 'time', or None to ask interactively.
    """
    dt = parser.parse(s)

    if mode is None:
        mode = input("Choose 'date' or 'time': ").strip().lower()
    if mode == "date":
        return print(dt.strftime("%x"))
    elif mode == "time":
        return print(dt.strftime("%X"))
    else:
        raise ValueError("Mode must be 'date' or 'time'.")
    

# parse_date_or_time("Jul 20, 1969 10:56 PM", "date")
# → "07/20/69"

# parse_date_or_time("Jul 20, 1969 10:56 PM", "time")
# → "22:56:00"

# ----------------------------------------------------------------------------------------


# def parse_date_only(s):
#     dt = parser.parse(s)
#     return dt.strftime(f"%{input('x for date or X for time: ')}")   # locale-formatted date
# # ----------------------------------------------------------------------------------------



# birth = dt.datetime.fromisoformat('1969-07-20 22:56')
# print(f'Birth date: {birth:%x}')
# print(f'Birth time: {birth:%X}')
# ------------------------------------------------------------------------------------------


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
    return filled

    # # filled = 'Jul 10, 1999 10:10 AM'
    # birth_dt = dt.datetime.strptime(filled, "%b %d, %Y %I:%M %p")
    # age_delta = dt.datetime.now() - birth_dt

    # days = age_delta.days
    # hours = age_delta.seconds // 3600
    # minutes = age_delta.seconds % 60
    # seconds = age_delta.total_seconds()
    
    # print(f'It has been {days} days, {hours} hours,{minutes} minutes, and {seconds} seconds since then.')
# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    parse_date_or_time(date_time()) # can replace 'time' with 'date'
    pass
# CHANGING