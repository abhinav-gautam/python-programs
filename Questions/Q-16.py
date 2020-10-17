import random
n=int(input("Enter No of Rows Of Matrix"))
m=int(input("Enter no of Columns of Matrix"))
a=[[random.random() for i in range(m)]for i in range(n)]
for i in range(m):
    for j in range(n):
        a[i][j]=int(input("Enter elements"))
print "Matrix is"
for i in range(m):
    for j in range(n):
        print a[i][j],
    print
c=0
print "Row Sum is"
for i in range(m):
    for j in range(n):
        c=c+a[i][j]
    print c
    c=0
s=0
print "Column Sum is"
for j in range(m):
    for i in range(n):
        s=s+a[i][j]
    print s
    s=0
print "Developed by Abhinav Kumar Gautam"   
        
    
