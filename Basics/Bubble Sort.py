def bubsort(a):
    t=0
    for i in range(len(a)+1):
        for j in range(i+1,len(a)):
            if (a[i]>a[j]):
                t=a[j]
                a[j]=a[i]
                a[i]=t
        print("list after iteration ",i+1,a)
    print("Sorted list is",a)
a=[]
n=int(input("enter no. of elements in your list"))
for i in range(0,n,1):
    x=int(input("Enter elements"))
    a.append(x)
print("Original list is",a)
bubsort(a)
