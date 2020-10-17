c=int(input("Enter"))
a=-1
b=1
l=[]
for i in range (1,c+1):
    d=a+b
    a=b
    b=d
    l.append(d)
print l
    
