from datetime import datetime

t1 = 'Sun 10 May 2999 13:54:36 -0700'
t2 = 'Sun 10 May 2015 13:54:36 -0000'

time_format = '%a %d %b %Y %H:%M:%S %z'

t1 = datetime.strptime(t1, time_format)
t2 = datetime.strptime(t2, time_format)

print(int(abs((t1-t2).total_seconds())))