a=[]
class insert:
    def __init__(self,a=0,n=0,ele=0,x=0):
        a=[]
        self.n=n
        self.ele=ele
        self.x=x
    def show(self):
        beg=0
        end=len(a)-1
        a.sort()
        for i in range(len(a)):
            mid=(beg+end)//2
            if(a[mid]<self.ele and self.ele<a[mid+1]):
                a.insert((mid+1),self.ele)
            elif(self.ele>a[beg] and self.ele<a[mid]):
                end=mid
            elif(self.ele>a[mid] and self.ele<a[end]):
                beg=mid
            if(self.ele>=a[len(a)-1]):
                a.append(self.ele)
            elif(self.ele<=a[0]):
                a.insert(0,self.ele)
        print(a)
    def enter(self):
        self.n=int(input("enter no. of elements in your list"))
        for i in range(0,self.n,1):
            self.x=int(input("Enter element"))
            a.append(self.x)
            a.sort()
        self.ele=int(input("enter element to be inserted"))
        
    

