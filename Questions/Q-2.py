a=int(input('Enter number in decimal'))
x=int(input('Enter your choice 1.Binary 2. Octal 3.Hexadecimal '))
if(x==1):
    l=[]
    while(a>0):
        d=a%2
        l.append(d)
        a=a//2
    print 'Decimal to Binary is'
    for i in range(len(l)-1,-1,-1):
        print l[i],
if(x==2):
    l=[]
    while(a>0):
        d=a%8
        l.append(d)
        a=a//8
    print 'Decimal to Octal is'
    for i in range(len(l)-1,-1,-1):
        print l[i],
if(x==3):
    l=[]
    while(a>0):
        d=a%16
        l.append(d)
        a=a//16
    print 'Decimal to Hexadecimal is'
    for i in range(len(l)-1,-1,-1):
        if(l[i]==9):
            l[i]='A'
        elif(l[i]==10):
            l[i]='B'
        elif(l[i]==11):
            l[i]='C'
        elif(l[i]==12):
            l[i]='D'
        elif(l[i]==13):
            l[i]='E'
        elif(l[i]==14):
            l[i]='F'
        elif(l[i]==15):
            l[i]='G'
        print l[i],
print ("Developed by Abhinav Kumar Gautam")
