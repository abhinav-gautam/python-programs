def bsearch(a,ele):
    beg=0
    end=len(a)-1
    while (beg<end):
        mid=(beg+end)//2
        if(a[mid]==ele):
            print ("The element is found at",mid+1,"position")
            break
        elif(ele>a[mid]):
            beg=mid+1
        elif(ele<a[mid]):
            end=mid-1
a=[]
n=int(input("enter no. of elements"))
for i in range(0,n,1):
    x=int(input())
    a.append(x)
a.sort()
ele=int(input("enter element to be searched"))
print('Your sorted list is')
print(a)
bsearch(a,ele)
        
            
