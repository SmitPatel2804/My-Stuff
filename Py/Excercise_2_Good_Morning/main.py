import time
recenttimeinhour=int(time.strftime("%H"))
recenttimeinminute=int(time.strftime("%M"))
recenttimeinsecond=int(time.strftime("%S"))
H = recenttimeinhour
M = recenttimeinminute
S = recenttimeinsecond
if(H>=00 and H<12):
    print("Good Morning Sir")
elif(H>=12 and H<18):
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")



