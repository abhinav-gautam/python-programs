a=input("Enter")
p=len(a)
for i in range(0,p):
    if(a[i]==a[p-1]):
        p=p-1
    else:
        print("It is not a plindrome")
        break
else:
    print("it is palindrome")
