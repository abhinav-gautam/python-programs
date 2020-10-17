def rotate(a):
    a.pop(n-1)
    a.insert(0,x)
    return a
a=[]
n=int(input("Enter range"))
for i in range(n):
    x=raw_input("Enter element")
    a.append(x)     
print "Old List",a
print "New list",rotate(a)
