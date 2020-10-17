def selectionsort(a):
    for k in range(len(a)):
        t=a[k]
        p=k    
        for j in range(k+1,len(a)):
            if (a[j]<t):
                t=a[j]
                p=j   
        a[p]=a[k]
        a[k]=t
        print "list after iteration ",k+1,a 
    print  "Sorted List is:",a 
def insertionsort(a):
    for i in range(1,len(a)):
        t=a[i]
        p=i-1
        while((p>=0) and (a[p]>t)):
            a[p+1]=a[p]
            p=p-1
            print "list after iteration ",i,a
        a[p+1]=t
        print "list after iteration ",i,a 
    print "Sorted list is",a 
a=[3,5,4,3,7,1,2]
print "Selection Sorting"
selectionsort(a)
print "Insertion Sorting"
insertionsort(a)
