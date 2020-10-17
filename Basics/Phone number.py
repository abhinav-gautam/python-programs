p=dict()
n=int(input("Enter no of names"))
for i in range(0,n):
    a=raw_input("Enter name")
    p[a]=int(input("Enter Phone number"))
b=raw_input("Enter name to search")
d=p.keys()
c=0
for i in range(0,len(d)):
    if(d[i]==b):
        print("Phone number of ",b,"is ",p[b])
        c=1
        break
if c==0:
    print("No such kind of person is in list")
