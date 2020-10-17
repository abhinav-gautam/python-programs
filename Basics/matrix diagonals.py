# To input any matrix and print both the diagonals
print("This programme is to print the diagonals of a square matrix : ")
n=int(input("Enter the number of element of the matrix : "))
x=[[(i*0) for i in range(0,n,1)] for j in range(0,n,1)]
print("Enter ",(n**2)," elements in the ",n,"x",n," matrix : ")
for i in range(0,n,1):
    for j in range(0,n,1):
        x[i][j]=int(input())
print("Your matrix is : ")
for i in range(0,n,1):
    for j in range(0,n,1):
        print(x[i][j],end=" ")
    print()
print("The values on left top diagonal is : ")
for i in range(0,n,1):
    print(x[i][i],end="  ")
print("The values on right top diagonal is : ")
for i in range(0,n,1):
    print(x[i][n-i-1],end="  ")
print ("Developed by Abhinav Kumar Gautam")
