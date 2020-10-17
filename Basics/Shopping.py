print("icode,price,item name,qty")
class Buy:
    def __init__(self,icode=0,price=0,item="ABC",qty=0):
        self.icode=icode
        self.price=price
        self.qty=qty
        self.item=item
        self.netprice=0
        self.discount=0
    def enter(self):
        self.icode=int(input("Enter item code"))
        self.item=input("Enter item name")
        self.price=int(input("Enter price"))
        self.qty=int(input("Enter quantity"))
    def finddisc(self):
        self.netprice=(self.price*self.qty)
        if (self.qty<=10):
            self.discount+=0
        elif(self.qty>=11 and self.qty<20):
            self.discount+=0.15*self.netprice
        elif (self.qty>=20):
            self.discount+=0.2*self.netprice
        self.netprice=(self.price*self.qty)-self.discount
    def showall(self):
        print("Item code is:",self.icode)
        print("Item name is:",self.item)
        print("Item quantity is:",self.qty)
        print("Item price is:",self.price)
        print("Discount is:",self.discount)
        print("Net price is:",self.netprice)
            
            
        
        
