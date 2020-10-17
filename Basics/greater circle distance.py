#great circle distance.
import math
r=int(input("Enter the radius : "))
x1=int(input("Enter the x coordinate of first point : "))
y1=int(input("Enter the y coordinate of first point : "))
x2=int(input("Enter the x coordinate of second point : "))
y2=int(input("Enter the y coordinate of second point : "))
a=r*(math.cos(math.sin(x1)))*(math.sin(x2))
b=(math.cos(x1))*(math.cos(x2))*(math.cos(y1-y2))
d=(r*a)+b
print(d,"is the greater circle distance.")
print ("Developed by Abhinav Kumar Gautam")
