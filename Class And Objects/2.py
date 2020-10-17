class Bank:
    def __init__(self,CNo,Cname,bal):
        #CNo=Customer number,Cname=Customer Name
        self.CNo=CNo
        self.Name=Cname
        self.bal=bal
    def deposit(self,bal):
        self.bal+=bal
    def withdraw(self,bal):
        if(bal>self.bal):
            print("Insufficient Fund")
        else:
            self.bal=bal
    def checkbal(self):
        return(self.bal)
    def __str__(self):
        return(str(self.CNo)+" "+str(self.Name)+" "+str(self.bal))
        
        
