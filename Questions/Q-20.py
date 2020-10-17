def line_intersect():
    while True:
        try:
            x=(c2-c1)/(m1-m2)
            y=(m2*c1-m1*c2)/(m1-m2)
            print "Point of intersection","(",x,",",y,")"
            break
        except ZeroDivisionError:
            print "Lines do not intersect"
            break    
x1=int(input("Enter x1"))
y1=int(input("Enter y1"))
a1=int(input("Enter a1"))
b1=int(input("Enter b1"))
x2=int(input("Enter x2"))
y2=int(input("Enter y2"))
a2=int(input("Enter a2"))
b2=int(input("Enter b2"))
m1=(b1-y1)/(a1-x1)
m2=(b2-y2)/(a2-x2)
c1=m1*x1-y1
c2=m2*x2-y2
if (m1/m2!=c1/c2):
    line_intersect()
else:
    print "Lines are coincident"
    if c1>0:
        print "Equation of line is :",m1,"x +"," y +",c1," = 0"
    else:
        print "Equation of line is :",m1,"x +"," y ",c1," = 0"
print "Developed by Abhinav Kumar Gautam"       
