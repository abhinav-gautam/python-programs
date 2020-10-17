def is_sorted(x):
    c=0
    l=len(x)
    for i in range(0,l-1,1):
        if x[i]>x[i+1]:
            c=c+1
    return (c)

# To print whether a list is in ascending order or not
print("This programme shows whether a list is sorted in ascending order or not : ")
n=int(input("Enter the number of elements in your list : "))
x=[i for i in range(0,n,1)]
print("Enter ",n," numbers in your list : ")
for i in range(0,n,1):
    x[i]=int(input())
c=is_sorted(x)
if c==0:
    print("True : ")
else :
    print("False : ")
print ("Developed by Abhinav Kumar Gautam")
    
