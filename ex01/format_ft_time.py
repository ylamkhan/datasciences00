"""
1- Time: lib in python for use time
        For use time : import time as t
        t.time(): Current timestamp (seconds since epoch)
        t.sleep(seconds): Pause execution for a given duration
        t.strftime(format, time_struct): Format time

2- The datetime module in Python provides classes
    for manipulating dates and times in both simple and
    complex ways. It allows you to work with dates,
    times, time intervals, and even time zones.

    from datetime import datetime
    import pytz

    datetime.datetime: The combination of date and time.
    datetime.date: Represents just the date (year, month, day).
    datetime.time: Represents just the time (hour, minute, second).
    datetime.timedelta: Represents a duration
    (difference between two dates or times).
    datetime.tzinfo: Represents time zone information
    (for advanced time zone handling).


    What is January 1, 1970 in Python and computing?
    It's called the Unix Epoch.
    💡 What is the Unix Epoch?
    The Unix Epoch is the date and time 00:00:00 UTC on January 1, 1970.
    It's the starting point for time in many operating systems and programming
    languages — including Python.

"""
import time
from datetime import datetime

text = "Seconds since January 1, 1970: "
print(f"{text}{time.time()} or {time.time():.15e} in scientific notation")
now = datetime.now()
formatted_date = now.strftime("%b %d %Y")
print(formatted_date)
