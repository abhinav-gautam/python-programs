def rotate(a):
    for i in range(len(a)):
        if i!=len(a)-1:
            b.insert(i+1,a[i])
        else:
            b.insert(0,a[len(a)-1])       
a=[]
n=int(input("Enter no. of elements"))
for i in range(n):
    x=raw_input('Element')
    a.append(x)
b=[]
rotate(a)
print b
        
