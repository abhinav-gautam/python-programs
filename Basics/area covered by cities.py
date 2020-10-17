def gcd(x1,x2,y1,y2):
    d=(6400)*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
    return d

def area(s1,s2,s3):
    s=(s1+s2+s3)/2
    ar=((s)*(s-s1)*(s-s2)*(s-s3))**(1/2)
    return ar

# To find the area enclosed by four cities
import math
print("This programme gives the area enclosed by four cities : ")
print("Atlanta, Georgia LATITUDE = N 35 45' 0.36\" LONGITUDE = W 84 23' 18.528\" : ")
print("Orlando, Florida LATITUDE = N 28 32' 18.328\" LONGITUDE = W 81 22' 44.256\" : ")
print("Savannah, Georgia LATITUDE = N 32 5' 1.014\" LONGITUDE = W 81 5' 59.445\" : ")
print("Charlotte, North Caroline LATITUDE = N 35 13' 47.996\" LONGITUDE = W 80 50' 24\" : ")
print("Earth's radius is taken as 6400 km : ")
xa=35+(45/60)+(0.36/60/60)
ya=84+(23/60)+(18.528/60/60)
xo=28+(32/60)+(18.328/60/60)
yo=81+(22/60)+(44.256/60/60)
xs=32+(5/60)+(1.014/60/60)
ys=81+(5/60)+(59.445/60/60)
xc=35+(13/60)+(47.996/60/60)
yc=80+(50/60)+(24/60/60)
xa=math.radians(xa)
ya=math.radians(ya)
xo=math.radians(xo)
yo=math.radians(yo)
xs=math.radians(xs)
ys=math.radians(ys)
xc=math.radians(xc)
yc=math.radians(yc)
dao=gcd(xa,xo,ya,yo)
dos=gcd(xo,xs,yo,ys)
dsc=gcd(xs,xc,ys,yc)
dca=gcd(xc,xa,yc,ya)
das=gcd(xa,xs,ya,ys)
areaaos=area(dao,dos,das)
areaasc=area(das,dsc,dca)
tarea=areaaos+areaasc
print()
print("The area enclosed by the four cities is : ",tarea," km square ")
print ("Developed by Abhinav Kumar Gautam")

