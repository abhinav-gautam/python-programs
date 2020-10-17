
import random
r1=int(input("Enter row of 1"))
c1=int(input("Enter column of 1"))
a=[[random.random()for row in range(r1)]for col in range(c1)]
for i in range (r1):
    for j in range (c1):
        a[i][j]=int(input("Enter:"))
r2=int(input("Enter row of 2"))
c2=int(input("Enter column of 2"))
b=[[random.random()for row in range(r1)]for col in range(c1)]
for i in range (r2):
    for j in range (c2):
        b[i][j]=int(input("Enter:"))
d=[[random.random()for row in range(r1)]for col in range(c1)]
if((c1==c2)and(r1==r2)):
    print ("Addition of matrix is")
    for i in range (r1):
        for j in range (c1):
            d[i][j]=b[i][j]*a[i][j]
            print(d[i][j],end="  ")
        print()
else:        
      print ('Matrix addition not possible')
