import time

unixtime = int(time.mktime(time.strptime('2019-12-04 19:31:40', '%Y-%m-%d %H:%M:%S')))

humantime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(unixtime))

print(unixtime)