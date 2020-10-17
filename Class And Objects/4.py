class ctm:
    def __init__(self,CN):
        self.CN=CN
        self.CNM=str(input("Customer Name"))
        self.qty=int(input("Quantity"))
        self.price=float(input("Price"))
    def input(self):
        self.CN=int(input("Customer Number"))
        self.CNM=str(input("Customer Name"))
        self.qty=int(input("Quantity"))
        self.price=float(input("Price"))
    def caldiscount():
        self.total=self.qty*self.price
        if(self.total<10000):
            self.dis=self.total*0.05
        else:
            self.dis=self.total*0.1
        self.ntp=self.total-self.dis
    def Bill(self):
        print("Customer Number ",self.CN,"         ","Customer Name ",self.CNM)
        print("Quantity      Price      Toatl     Discount     Net Price")
        print(self.qty,"     ",self.price,"     ",self.total,"     ",self.dis,"     ",self.ntp)
      
        
    
        
            
            
        
        
