def cumsum(x):
    sum=0
    l=len(x)
    for i in range(0,l,1):
        sum=sum+x[i]
        x[i]=sum
    return (x)

# To print the cumulative sum of a given list.
n=int(input("Enter the number of elements in your list : "))
x=[i for i in range(0,n,1)]
print("Enter ",n," numbers in your list : ")
for i in range(0,n,1):
    x[i]=int(input())
sum=cumsum(x)
print("The cumulative sum of your list is : ")
for i in range(0,n,1):
    print(x[i],end=" ")
print ("Developed by Abhinav Kumar Gautam")
    
