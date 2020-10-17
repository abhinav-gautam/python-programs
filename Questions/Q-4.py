def primeno(n):
    for i in range(2,n,1):
        c=0
        for j in range(2,i,1):
            if(i%j==0):
                c=1
                break
        if(c==0):
            print(i)
n=int(input('Enter range'))
print('Prime numbers upto your range are:')
primeno(n)
