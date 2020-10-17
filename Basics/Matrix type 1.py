r=int(input("Enter No of rows"))
c=int(input("Enter No of columns"))
l=list(range(c*r))
for i in range (0,r*c):
    l[i]=input("Enter")
for i in range (0,r*c):
    if(i%r==0):
        print()
        print (l[i],end="   ")
    
