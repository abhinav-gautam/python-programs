n=int(input("Enter Number Of Students"))
a=[]
for i in range(n):
    rno=int(input("Enter Roll Number"))
    nm=input("Enter Name")
    per=float(input("Enter percentage"))
    a.append([rno,nm,per])
for i in range(n):
    for j in range(i+1,n):
        if(a[i][2]<a[j][2]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
print("Rank   Roll No   Name   Percentage")
for i in range(n):
    print(" ",i+1,"\t",a[i][0],"\t","",a[i][1],"\t",a[i][2])
