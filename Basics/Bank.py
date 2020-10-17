while 1:
    a=input("Do you want to calculate (a)Time Period or (b)EMI :")
    if (a=="a" or a=="A"):
        c=0
        i=0
        il=[]
        p=float(input("Enter Principal Amount:"))
        am=float(input("Enter Amount you want to along with intrest:"))
        r1=float(input("Enter rate of intrest:"))
        while p>0:
            i=p*(r1/100)
            p=p-am
            c+=1
            il.append(i)
            print("Intrest for:")
            si=0
        for i in range(c):
            print ("Month",i+1,"is :Rs",il[i])
            si+=il[i]
        print("Total Intrest: Rs",si)
        print("Total Time:",c," Months")
    elif (a=="b" or a=="B"):
        import math
        p=float(input("Enter Principal Amount:"))
        t=int(input("Enter time period in months:"))
        r=float(input("Enter rate of intrest:"))
        emi=(p/(1-((100/(100+r/12))**t)))*r/12/100
        ti=(emi*t)-p
        print("EMI:Rs",math.ceil(emi))
        print("Total Intrest: Rs",math.ceil(ti))
    b=input("Do you want to continue (y/n)")
    if b=="n":
        break

   
    

    
    
        
    
        

