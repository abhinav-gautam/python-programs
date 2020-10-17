class employee:
    def __init__(self,en=0,name="",desg="",add="",pn=0):
        self.en=en
        self.name=name
        self.desg=desg
        self.add=add
        self.pn=pn
    def getdata(self):
        self.en=int(input("Enter emplyee number"))
        self.name=raw_input("Enter emplyee name")
        self.desg=raw_input("Enter designation")
        self.add=raw_input("Enter address")
        self.pn=int(input("Enter phone number"))
    def putdata(self):
        print "Emplyee number",self.en
        print "Emplyee name",self.name
        print "Designation",self.desg
        print "Address",self.add
        print "Phone number",self.pn
class salary(employee):
    def __init__(self,en=0,name="",desg="",add="",pn=0,bp=0,da=0,hra=0,gp=0,pf=0,it=0,np=0):
        employee.__init__(self,en=0,name="",desg="",add="",pn=0)
        self.bp=bp
        self.da=da
        self.hra=hra
        self.gp=0
        self.pf=pf
        self.it=it
        self.np=0
    def getdata1(self):
        a.getdata()
        self.bp=float(input("Enter basic pay"))
        self.da=float(input("Enter Da"))
        self.hra=float(input("Enter HRA"))
        self.pf=float(input("Enter PF"))
        self.it=float(input("Enter income tax"))
    def calculate(self):
        self.gp+=self.bp+self.da+self.hra
        self.np+=self.gp-self.pf-self.it
    def display(self):
        a.putdata()
        print "Basic pay",self.bp
        print "DA",self.da
        print "HRA",self.hra
        print "Gross Pay",self.gp
        print "PF",self.pf
        print "Income tax",self.it
        print "Net Pay",self.np
a=employee()
a=salary()
a.getdata1()
a.calculate()
a.display()
        
    
        

    
