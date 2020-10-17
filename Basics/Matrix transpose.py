import random
n=int(input("Enter no of rows"))
m=int(input("Enter no of columns"))
a=[[random.random()for rows in range(n)]for col in range(m)]
for i in range(n):
    for j in range(m):
        a[i][j]=int(input("Enter elements"))
print("Matrix is")
for i in range(n):
    for j in range(m):
        print(a[i][j],end="  ")
    print()

print("Transpose of Matrix is")
for j in range(n):
    for i in range(m):
        print(a[i][j],end="  ")
    print()
        
