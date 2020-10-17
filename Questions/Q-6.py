import math
class difftime:
    def __init__(self,h1=0,h2=0,m1=0,m2=0,s1=0,s2=0):
        self.h1=float(input("Enter 1st time in hours:"))
        self.m1=int(input("Enter 1st time in minutes:"))
        self.s1=int(input("Enter 1st time in seconds:"))
        self.h2=float(input("Enter 2nd time in hours:"))
        self.m2=int(input("Enter 2nd time in minutes:"))
        self.s2=int(input("Enter 2nd time in seconds:"))
        if self.h1>=self.h2:
            self.ts=math.fabs(self.s1-self.s2)
            self.tm=math.fabs(self.m1-self.m2)-self.ts//60
            self.th=math.fabs(self.h1-self.h2)-self.tm//60
    def display(self):
        print 'Sum of time is:', self.th,'hrs.',self.tm%60,'min',self.ts%60,'sec'
a=difftime()
a.display()
        
        
        
        
