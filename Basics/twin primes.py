#To find all the twin primes less than 1000
print("This programme is to find all the twin primes less then 1000 : ")
c=0
d=0
print("The list of twin primes are : ")
for i in range(2,998,1):
    for j in range(1,i+1,1):
        if i%j==0:
            c=c+1
    for k in range(1,i+3,1):
        if (i+2)%k==0:
            d=d+1
    if c==2 and d==2:
        print("(",i,",",(i+2),")",end="  ;  ")
    c=0
    d=0
print ("Developed by Abhinav Kumar Gautam")
    
