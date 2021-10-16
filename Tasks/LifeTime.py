import datetime

def pro(x):
    x = x.split('.')
    date = datetime.date(int(x[2]),int(x[1]),int(x[0]))
    return date

x1 = pro(input(('Write day when you born: \'Day.Mounth.Year\'\n\n')))
xy = datetime.datetime.now()
x11 = xy.date()
x2: datetime.timedelta = x11 - x1
print(x2.days)