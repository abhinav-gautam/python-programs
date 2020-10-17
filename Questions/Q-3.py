class complex:
    def __init__(self,x=0,y=0,a=0,b=0):
        self.x=x
        self.y=y
        self.a=a
        self.b=b
        self.sum1=0
        self.sum2=0
    def input(self):
        self.x=int(input("Enter First Real part"))
        self.y=int(input("Enter First Imaginary part"))
        self.a=int(input("Enter Second Real part"))
        self.b=int(input("Enter Second Imaginary part"))
    def sum(self):
        self.sum1+=self.x+self.a
        self.sum2+=self.y+self.b
    def display(self):
        print "Sum is",self.sum1,"+i(",self.sum2,")"
a=complex()
a.input()
a.sum()
a.display()
