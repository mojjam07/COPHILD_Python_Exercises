import os
from datetime import date
from datetime import time
import time
from datetime import datetime
import calendar

#os.mkdir('mojjam') # create directory called 'mojjam'

#os.makedirs('mojjam/mubby') # create directories

#os.chdir('mojjam') # change directories

#print(os.getcwd()) # get current directory

#os.rmdir('mubby') # delete a directory

#os.makedirs('mubby/mushjam')

#os.removedirs('mubby/mushjam') # delete more than one directories

#create_dir = os.system('mkdir mojjam') #Another method with system()

#print(os.listdir()) # list files & directories

print(os.uname())

### for datetime module

today = date.today()

print("Today:", today)
print("Today:", today.year)
print("Today:", today.month)
print("Today:", today.day)

#print(date(2019, 11, 4))

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)
print("Week day:", d.weekday()) # Monday - Sunday reps 0-6
print("Week day:", d.isoweekday()) # Monday - Sunday reps 1-7

# Creating time object
'''
t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
'''

print(time.sleep(2))
print("See me here!")
print(time.ctime())

print("Today:", datetime.today())
print("Now", datetime.now())
print("UTCnow:", datetime.utcnow())
#print("Timestamp", datetime.timestamp(2022, 10, 4, 15, 55))

# Date and Time formatting

d = date(2020, 1, 4)
print("Strftime", d.strftime('%Y/%m/%d'))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime('%y/%B/%d %H:%M:%S'))

#### Working with calendar

#print(calendar.calendar(2000))

print(calendar.prcal(2020))

print(calendar.month(2024, 5))

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.prmonth(2024, 6))

print(calendar.weekday(2020, 12, 13))

print(calendar.weekheader(2))

