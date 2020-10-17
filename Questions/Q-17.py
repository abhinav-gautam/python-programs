import random
def summajordiagonals():
    a=[[random.random() for i in range(m)]for i in range(n)]
    for i in range(m):
        for j in range(n):
            a[i][j]=int(input("Enter elements"))
    print "Matrix is"
    for i in range(m):
        for j in range(n):
            print a[i][j],
        print
    print "Sum of major diagonal"
    s=0
    for i in range(m):
        for j in range(n):
            if i==j:
                s+=a[i][j]
    print s
n=int(input("Enter No of Rows Of Matrix"))
m=int(input("Enter no of Columns of Matrix"))
summajordiagonals()
print "Developed by Abhinav Kumar Gautam"   
