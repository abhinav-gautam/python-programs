class iteminfo:
    def __init__(self,icode=0,price=0,item="ASD",qty=0):
        self.icode=icode
        self.price=price
        self.item=item
        self.qty=qty
        self.discount=0
        self.netprice=0
    def buy(self):
        self.icode=int(input("Enter item code"))
        self.item=str(input("Enter item name"))
        self.price=float(input("Enter price"))
        self.qty=int(input("Enter quantity"))
    def finddisc(self):
        self.netprice=self.price*self.qty
        if(self.qty<=10):
            self.discount=0
        elif(self.qty>11 and self.qty<20):
            self.discount+=0.15*self.price
        elif(self.qty>=20):
            self.discount+=0.2*self.price
        self.netprice=self.netprice-self.discount
    def showall(self):
        print "item code is",self.icode
        print "item name is",self.item
        print "item quantity is",self.qty
        print "Price is",self.price
        print "Discount is",self.discount
        print "Netprice is",self.netprice
            
    
