# To find marsene prime numbers
c=0
print("The marsenne prime numbers are : ")
for i in range(1,32,1):
    n=(2**i)-1
    for j in range(1,n+1,1):
        if n%j==0:
            c=c+1
    if c==2:
        print(i,"-----------------",n)
    c=0
print ("Developed by Abhinav Kumar Gautam")
    
    
