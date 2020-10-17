n=float(input('Enter number'))
l=[]
while n!=0:
    if n%2==0:
        l.append(0)
        n=n//2
    else:
        l.append(1)
        n=n//2
l.reverse()
print 'binary is '
for i in  range(len(l)):
    print l[i],

