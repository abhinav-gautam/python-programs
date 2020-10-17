def insertionsort(a):
    for i in range(1,len(a)):
        t=a[i]
        p=i-1
        while((p>=0) and (a[p]>t)):
            a[p+1]=a[p]
            p=p-1
        a[p+1]=t
        print("list after iteration ",i,a)
    print("Sorted list is",a)
a=[]
n=int(input("enter no. of elements in your list"))
for i in range(0,n,1):
    x=int(input("Enter elements"))
    a.append(x)
print("Original list is",a)
insertionsort(a)
