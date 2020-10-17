def palindrome(x):
    r=0
    rev=0
    t=x
    while x>0:
        r=x%10
        r=r*10+r
        x=x//10
    if t==r:
        return(1)
    else:
        return(0)

def prime(x):
    c=0
    for i in range(1,x+1,1):
        if x%i==0:
            c=c+1
    if c==2:
        return(1)
    else:
        return(0)

# To print the first hundred palindrome primes
print("first hundred palindromic primes are (takes time.) : ")
z=0
n=2
while z!=100:
    p=prime(n)
    pa=palindrome(n)
    if p==1 and pa==1:
        z=z+1
        if z<=10:
            print(n,end=" ")
        else:
            z=1
            print()
            print(n,end=" ")
    n=n+1
print ("Developed by Abhinav Kumar Gautam")
