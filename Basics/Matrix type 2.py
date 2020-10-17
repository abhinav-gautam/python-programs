import random
r=int(input("Enter rows"))
c=int(input("Enter columns"))
a=[[random.random()for row in range(r)]for col in range(c)]
for i in range (r):
    for j in range(c):
        a[i][j]=input('Enter:')
for i in range (r):
    for j in range(c):
        print (a[i][j],end="    ")
    print()
