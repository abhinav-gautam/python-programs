class stud:
    def __init__(self):
        self.students=[]
    def addstudent(self,rno,name,per):
        self.students.append([rno,name,per])
    def __str__(self):
        return(str(self.students)+"No of students"+len(students))
class result(stud):
    def topper(self):
        t=-1
        per=0
        l=len(self.students)
        for i in range(l):
            if(self.students[i][2]>per):
                t=i
                per=self.students[i][2]
        print "topper",self.students[t][0]
        print "name",self.students[t][1]
        print "per",self.students[t][2]
        
        
