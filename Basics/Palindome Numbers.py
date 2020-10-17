a=int(input("Enter Range"))
for i in range(1,a+1):
    s=0
    t=i
    while (t>0):
        d=t%10
        s=d+s*10
        t=t//10
    if(i==s):
        print("Palindome Numbers are",i)
