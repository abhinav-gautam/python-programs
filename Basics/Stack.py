class stack:
    def __init__(self):
        self.stk=[]
    def push(self,ele):
        self.stk.append(ele)
        self.top=len(self.stk)-1
    def pop(self):
        if(self.stk==[]):
            print("Stack is underflow")
        else:
            x=self.stk.pop()
            self.top-=1
            return x
    def display(self):
        if (self.top!=-1):
            for i in range(self.top,-1,-1):
                print(self.stk[i])
s=stack()
x=0
while(x!=4):
    print "press 1-pop, 2-push, 3-display, 4-exit"
    x=int(input("Enter choice"))
    if (x==1):
        s.pop()
    elif(x==2):
        ele=raw_input("Enter element")
        s.push(ele)
    elif(x==3):
        s.display()
