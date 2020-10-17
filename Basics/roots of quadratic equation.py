#roots of quadratic equation.
import math
print("let the quadratic equation is in the form ax2+bx+c=0.")
a=int(input("Enter the value of coeeficient of x2 : "))
b=int(input("Enter the value of coeeficient of x : "))
c=int(input("Enter the value of constant c : "))
e=(b**2)-4*a*c
d=(e)**1/2
if d==0:
    print("roots are equal.")
    r=(-b+d)/2*a
    print("roots are :",r," and ",r)
elif d>0:
    print("roots are real,this equation has two roots.")
    r1=(-b+d)/2*a
    r2=(-b-d)/2*a
    print("roots are :",r1,"and",r2)
elif d<0:
    print("roots are imaginary.")
print ("Developed by Abhinav Kumar Gautam")

