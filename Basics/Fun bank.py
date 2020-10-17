import math
class time:
    def __init__(self,p=0,r1=0,am=0):
        self.p=p
        self.r1=r1
        self.am=am
    def enter(self):
        self.p=float(input("Enter Principal Amount:"))
        self.am=float(input("Enter Amount you want to along with intrest:"))
        self.r1=float(input("Enter rate of intrest:"))
    def calculate_time(self):
        c=0
        i=0
        il=[]
        while self.p>0:
            i=self.p*(self.r1/100)
            self.p=self.p-self.am
            c+=1
            il.append(i)
        print("Intrest for:")
        si=0
        for i in range(c):
            print ("Month",i+1,"is :Rs",il[i])
            si+=il[i]
        print("Total Intrest: Rs",si)
        print("Total Time:",c," Months")
class emi(time):
    def __init__(self,p=0,r1=0,t=0):
        time. __init__(self,p,r1)
        self.t=t
    def enter(self):
        self.p=float(input("Enter Principal Amount:"))
        self.t=int(input("Enter time period in months:"))
        self.r=float(input("Enter rate of intrest:"))
    def calculate_emi(self):
        emi=(self.p/(1-((100/(100+self.r/12))**self.t)))*self.r/12/100
        ti=(emi*t)-self.p
        print("EMI:Rs",math.ceil(emi))
        print("Total Intrest: Rs",math.ceil(ti))
    
    
    
