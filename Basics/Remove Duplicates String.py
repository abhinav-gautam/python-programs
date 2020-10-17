def remove_duplicates_string(a,b):
    c=0
    d=[]
    for i in range(len(a)):
        for j in range(0,len(b)):
            if a[i]==b[j]:
                b[j]=0
                c=1
        if c==1:
            d.append(a[i])
            a[i]=0
        c=0
    print("Unique elements")
    for i in a:
        if i!=0:
            print(i,end="")
    print()
    for i in b:
        if i!=0:
            print(i,end="")
    print()
    print("Duplicate elements")
    for i in d:
        if i!=0:
            print(i,end="")
    
def remove_duplicates(a,b):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                a[j]=0
    remove_duplicates_string(a,b)
a=list(input().lower())
b=list(input().lower())
remove_duplicates(a,b)
