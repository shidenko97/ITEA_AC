# import datetime
#
# print(dir(datetime))
#
# datetime_object = datetime.datetime.now()
# print(datetime_object)
#
# date_object = datetime.date.today()
# print(date_object)
#
# d = datetime.date(year=2019, month=4, day=13)
# print(d)

from datetime import date, datetime

# from datetime import *
a = date(2019, 4, 13)
print(a)
today = date.today()

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
my_datetime_object = time(11, 34, 56)
print("b =", my_datetime_object)
# time(hour, minute and second)
c = time(hour=11, minute=34, second=56)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

from datetime import time

a = time(11, 34, 56)
print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)


from datetime import datetime, timedelta

# datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)
# datetime(year, month, day, hour, minute, second, microsecond)
my_datetime_object = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(my_datetime_object)
my_date = my_datetime_object.strftime("%d-%m-%y")
new_date = my_datetime_object.strftime("%A %d. %B %Y")

my_datetime_obj = datetime.strptime("28-11-17", "%A %d. %B %Y")
datetime.strptime("Tuesday 28. November 2017", "%A %d. %B %Y") - timedelta(
    hours=30
)
pass
