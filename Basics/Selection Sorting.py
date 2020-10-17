def selectionsort(a):
    for k in range(n):
        t=a[k]
        p=k    
        for j in range(k+1,n):
            if (a[j]<t):
                t=a[j]
                p=j   
        a[p]=a[k]
        a[k]=t
        print("list after iteration ",k+1,a)
    print ("Sorted List is:",a)
n=int(input("Enter No of elements"))
a=[]
for i in range(n):
    e=int(input("Enter Element"))
    a.append(e)
print ("Original list is",a)
selectionsort(a)
        
