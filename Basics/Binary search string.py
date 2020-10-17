def bsearch(a,ele):
    beg=0
    end=len(a)-1
    for i in range(0,len(a)):
        mid=(beg+end)//2
        if(a[mid]==ele):
            print("Element is found at",mid+1,"position")
            break
        elif(a[mid]>ele):
            end=mid-1
        elif(a[mid]<ele):
            beg=mid+1
        elif(beg>=end):
            print("Element not found")
    
a=[]
n=int(input("enter no. of elements in your list"))
for i in range(0,n,1):
    x=input("Enter elements")
    a.append(x)
a.sort()
print("Original list is",a)
ele=input("enter element to be searched")
bsearch(a,ele)
        
            
