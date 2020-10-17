class ITEMINFO:
    def __init__(self,ICode=0,Item=0,Price=0,Qty=0,Disc=0,Netprice=0):
        self.ICode=ICode
        self.Item=Item
        self.Price=Price
        self.Qty=Qty
        self.Disc=0
        self.Netprice=0
    def Buy(self):
        self.ICode=int(input('Enter item code:'))
        self.Item=raw_input('Enter item name:')
        self.Price=float(input('Enter price:'))
        self.Qty=int(input('Enter quantity in stock:'))
    def FindDisc(self):
        self.Disc=0
        self.Totalprice=(self.Price*self. Qty)
        if(self.Qty<=10):
            self.Disc=0
            self.Netprice+=(self.Price*self.Qty)-self.Disc
        elif(10<self.Qty<=20):
            self.Disc=15
            self.Netprice+=(self.Price*self.Qty)-self.Disc
        elif(20<=self.Qty):
            self.Disc=20
            self.Netprice=(self.Price*self.Qty)-self.Disc
    def ShowAll(self):
        print('Item Code:',self.ICode)
        print('Item name:',self.Item)
        print('Price:',self.Price)
        print('Quantity:',self.Qty)
        print('Discount:',self.Disc)
        print('Totalprice:',self.Totalprice)
        print('Netprice:',self.Netprice)
ob=ITEMINFO()
ob.Buy()
ob.FindDisc()
ob.ShowAll()
        
        
        
        
        
