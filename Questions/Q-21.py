n=int(input("Enter no of elements in list."))
a=[]
for i in range(n):
    a.append(int(input("Enter element")))
print "Original list is",a
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print "New list is",b
