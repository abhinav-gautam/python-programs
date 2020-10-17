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
q=max(a)
s=max(q)
print s
print "Developed by Abhinav Kumar Gautam"   
