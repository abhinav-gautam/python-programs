def descending(x,n):
    t=0
    # by selection sorting
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            if x[i]<x[j]:
                t=x[i]
                x[i]=x[j]
                x[j]=t
    return (x)

# To sort a list in descending order
print("This programme sorts a list in descending order : ")
n=int(input("Enter the number of elements in the list : "))
x=[(i*0) for i in range(0,n,1)]
for i in range(0,n,1):
    x[i]=int(input())
x=descending(x,n)
print("The list in descending order is : ")
for i in range(0,n,1):
    print(x[i],end=" ")
print ("Developed by Abhinav Kumar Gautam")
