n=int(input("Enter the number of years"))
p=dict()
for i in range(n):
    a=int(input("Enter year"))
    p[a]=input("Enter Population")
b=p.keys()
print()
print("Population Information")
print("Year","\t","Population")
for i in b:
    print(i,"\t",p[i])
    
