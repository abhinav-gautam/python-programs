# To print the upper triangle matrix
print("This programme prints the upper triangle matrix of a square matrix : ")
n=int(input("Enter the number of elements in one side of the matrix : "))
x=[[(i*0) for i in range(0,n,1)] for j in range(0,n,1)]
print("Enter ",(n**2)," elements in the ",n,"x",n," matrix : ")
for i in  range(0,n,1):
    for j in range(0,n,1):
        x[i][j]=input()
print("Your matrix is : ")
for i in range(0,n,1):
    for j in range(0,n,1):
        print(x[i][j],end="  ")
    print()
print("The upper triangle of the matrix is : ")
for i in range(0,n,1):
    for j in range(0,n,1):
        if j>=i:
            print(x[i][j],end="  ")
        else:
            print(" ",end="  ")
    print()
print ("Developed by Abhinav Kumar Gautam")
