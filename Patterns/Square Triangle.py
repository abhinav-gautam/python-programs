n=int(input("Enter the range"))
for i in range(1,n+1,1):
        for k in range(n-i,0,-1):
            print(end="  ")
        for d in range(1,i+1,1):
            print((2**(d-1)),end=" ")
        for j in range(i-1,0,-1):
            print((2**(j-1)),end=" ")
        print()
