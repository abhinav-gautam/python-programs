def delel(a,ele):
    c=pos-1
    for i in range(c,len(a)-1):
        a[i]=a[i+1]    
a=[]
n=int(input("enter no. of elements in your list"))
for i in range(0,n,1):
    x=input("Enter element")
    a.append(x)
a.sort()
print("List before Deletation",a)
ele=input("Enter Element to delete")
for i in range(len(a)):
    if(a[i]==ele):
        pos=i+1
delel(a,ele)
b=[]
for i in range(len(a)-1):
    b.append(a[i])
print("List after Deletation",b)
