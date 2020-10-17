def Bubblesort():
    t=0
    for i in range(len(a)+1):
        for j in range(i+1,len(a)):
            if (a[i][2]>a[j][2]):
                t=a[j]
                a[j]=a[i]
                a[i]=t
    print "Item code        Item Name       Price       Quantity"
    
    for i in range(len(a)):
        print a[i][0],"\t",a[i][1],"\t",a[i][2],"\t",a[i][3]
def Insertionsort():
    for i in range(1,len(a)):
        t=a[i][3]
        p=i-1
        y=a[i]
        while((p>=0) and (a[p][3]<t)):
            a[p+1]=a[p]
            p=p-1
        a[p+1]=y
    print "Item code        Item Name       Price       Quantity"
    for i in range(len(a)):
        print a[i][0],"\t",a[i][1],"\t",a[i][2],"\t",a[i][3]
a=[]
n=int(input("Enter No Of Elements"))
for i  in range(n):
    ina=raw_input("Enter Item Name")
    ic=int(input("Enter item code"))
    pr=float(input("Enter price"))
    qty=int(input("Enter Quantity"))
    a.append([ina,ic,pr,qty])
print "In ascending order of price using bubble sort"
Bubblesort()
print "In descending order of qty using insertion sort"
Insertionsort()

