n=int(input("Enter total no of pair of points"))
a=[]
for i in range(n):
    print "Enter x coordinate of point",i+1,
    x=int(input())
    print "Enter y coordinate of point",i+1, 
    y=int(input())
    print "Enter z coordinate of point",i+1, 
    z=int(input())
    a.append([x,y,z])
s1=[]
s2=[]
for i in range(n):
    for j in range(i+1,n):
        d=((a[j][0]-a[i][0])**2+(a[j][1]-a[i][1])**2+(a[j][2]-a[i][2])**2)**0.5
        s1.append([i,j,d])
        s2.append(d)
m=min(s2)
c=[]
for i in range(len(s2)):
    if m==s1[i][2]:
        p1=s1[i][0]
        p2=s1[i][1]
        c.append([p1,p2])
print "Minimum distance between the points",
for i in range(len(c)):
    print a[c[i][0]],"and",a[c[i][1]],",",
print "is",m
print "Developed by Abhinav Kumar Gautam"   
