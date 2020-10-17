class errors(Exception):
    def error(self):
        print "Enter Correct Value"
    def error1(self):
        print "Enter date earlier than today's date"
    def error2(self):
        print "This is today's date"
import time
a=time.strftime("%d/%m/%Y")
pd=a.split("/")
print "Enter date earlier than today's date"
while True:
    try:
        d=int(input("Enter Date:"))
        m=int(input("Enter Month:"))
        y=int(input("Enter Year:"))
        if d>int(pd[0]) and m>int(pd[1]) and y>=int(pd[2]):
            raise errors()
        if d>31 or d<0 or m>12 or m<0 or y>int(pd[2]) or y<0:
            raise errors()
        if m==int(pd[1]) and d==int(pd[0]):
            raise errors()
        else:
            break
    except errors,a:
        if d>int(pd[0]) and m>int(pd[1]) and y>=int(pd[2]):
            a.error1()
        elif d>31 or d<0 or m>12 or m<0 or y>int(pd[2]) or y<0:
            a.error()
        if m==int(pd[1]) and d==int(pd[0]):
            a.error2()
        
        
cm=m
if cm in [1,3,5,7,8,10,12]:
    nd=32-d
elif cm in [4,6,9,11]:
    nd=31-d
else:
    if y%4==0:
        nd=30-d
    else:
        nd=29-d   

while 1:
    if cm==int(pd[1]):
        if m in [1,3,5,7,8,10,12]:
            td=nd+int(pd[0])-31
            break
        elif m in [4,6,9,11]:
            td=nd+int(pd[0])-30
            break
        else:
            if y%4==0:
                td=nd+int(pd[0])-29
                break
            else:
                td=nd+int(pd[0])-28
                break  
    if cm in [1,3,5,7,8,10,12] and cm!=int(pd[1]):
        nd+=31
        cm+=01
    if cm in [4,6,9,11] and cm!=int(pd[1]):
        nd+=30
        cm+=01
    if cm==2 and cm!=int(pd[1]):
        if y%4==0:
            nd+=29
            cm+=01
        else:
            nd+=28
            cm+=01
    if cm>12:
        cm=1        
if m<=int(pd[1]) or int(pd[2])-y>1:
    if int(pd[2])-y>1:
        td+=((int(pd[2])-y-1)*365)
    else:
        td+=((int(pd[2])-y)*365)
ny=td/365
nm=0
nnd=0
if (td%365)>=30:
    nm=(td%365)/30
    nnd=(td%365)%30
else:
    nnd=(ny%365)/30
if ny!=0:
    print ny,"Year(s)",
if nm!=0:
    print nm,"Month(s)",
if nnd!=0:
    print nnd,"Day(s) passed"
if m==int(pd[1]) and d!=int(pd[0]):
    print int(pd[0])-d+1,"Day(s) Passed"
print "Developed By Abhinav Gautam"






