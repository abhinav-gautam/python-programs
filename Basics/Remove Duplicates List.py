def remove_duplicates(x,n):
    c=0
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            if x[i]==x[j]:
                x[j]=0
                c=1
        if c==1:
                x[i]=0
        c=0
    return(x)

# To remove all the duplicate values in a list
n=int(input("Enter the number of elements : "))
x=[(i*0) for i in range(0,n,1)]
print("Enter the ",n," values in the list : ")
for i in range(0,n,1):
    x[i]=int(input())
x=remove_duplicates(x,n)
print("The unique list is : ")
for i in  range(0,n,1):
    if x[i]!=0:
        print(x[i])
print ("Developed by Abhinav Kumar Gautam")
