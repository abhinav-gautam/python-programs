class sumdist:
    def __init__(self,f1=0,f2=0,i1=0,i2=0,t=0):
        self.f1=float(input("Enter 1st distance in feet:"))
        self.i1=int(input("Enter 1st distance in inches:"))
        self.f2=float(input("Enter 2nd distance in feet:"))
        self.i2=int(input("Enter 2nd distance in inches:"))
        self.ti=self.i1+self.i2
        self.tf=self.f1+self.f2+self.ti//12 
    def display(self):
        print 'Sum of distances in feet is:', self.tf,'ft.',self.ti%12,'in'
a=sumdist()
a.display()
        
        
        
        
