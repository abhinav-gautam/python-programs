class queue:
    def __init__(self):
        self.que=[]
    def push(self,ele):
        self.que.append(ele)
        self.top=len(self.que)-1
    def pop(self):
        if(self.que==[]):
            print("queue is underflow")
        else:
            del(self.que[0])
            self.top-=1
            return x
    def display(self):
        if (self.top!=-1):
            for i in range(0,self.top+1,1):
                print(self.que[i])
s=queue()
x=0
while(x!=4):
    print "press 1-pop, 2-push, 3-display, 4-exit"
    x=raw_input("Enter choice")
    if (x==1):
        s.pop()
    elif(x==2):
        ele=raw_input("Enter element")
        s.push(ele)
    elif(x==3):
        s.display()
