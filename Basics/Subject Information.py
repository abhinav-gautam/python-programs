n=int(input("Enter the number of subjects"))
p=dict()
for i in range(n):
    a=input("Enter subject")
    p[a]=input("Enter Head of Department")
b=p.keys()
print()
print("Department Information")
print("Subject","\t","Head of Department")
for i in b:
    print(i,"\t","       ",p[i])
