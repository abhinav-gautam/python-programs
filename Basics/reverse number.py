a=int(input('Enter number'))
l=[]
while(a>0):
    x=a%10
    l.append(x)
    a=a//10
for i in range(len(l)):
    print l[i],
