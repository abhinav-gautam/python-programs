def insertele(a,ele):
    beg=0
    end=len(a)-1
    i=0
    if(ele>=a[len(a)-1]):
        a.append(ele)
    elif(ele<=a[0]):
        a.insert(0,ele)
    else:
        while beg<=end:
            mid=(beg+end)//2
            if(a[mid]<ele and a[mid+1]>ele):
                a.insert(mid+1,ele)
                break
            elif(ele<a[mid]):
                end=mid-1
            elif(ele>a[mid]):
                beg=mid+1   
a=[]
n=int(input("enter no. of elements in your list"))
for i in range(0,n):
    x=int(input("Enter element"))
    a.append(x)
a.sort()
ele=int(input("enter element to be inserted"))
print "List before insertion",a 
insertele(a,ele)
print "List after insertion",a
