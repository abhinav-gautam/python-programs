#area of regular polygon.
import math
n=int(input("Enter the number of sides : "))
l=int(input("Enter the length of sides : "))
p=math.radians(180/n)
a=(n*(l**2))/(4*math.tan(p))
print(a,"is the area of polygon having ",n, "sides.")
print ("Developed by Abhinav Kumar Gautam")
