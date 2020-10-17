#area of the triangle.
import math
x1=int(input("Enter the x coordinate of first point : "))
y1=int(input("Enter the y coordinate of first point : "))
print("first point is""(",x1,",",y1,")")
x2=int(input("Enter the x coordinate of second point : "))
y2=int(input("Enter the y coordinate of second point : "))
print("second point is""(",x2,",",y2,")")
x3=int(input("Enter the x coordinate of third point : "))
y3=int(input("Enter the y coordinate of third point : "))
print("third point is""(",x3,",",y3,")")
e=(x2-x1)**2+(y2-y1)**2
f=(x3-x2)**2+(y3-y2)**2
g=(x3-x1)**2+(y3-y1)**2
d1=math.sqrt(e)
d2=math.sqrt(f)
d3=math.sqrt(g)
s=(d1+d2+d3)/2
a=math.sqrt((s*(s-d1)*(s-d2)*(s-d3)))
print(a,"is the area of triangle.")
print ("Developed by Abhinav Kumar Gautam")



