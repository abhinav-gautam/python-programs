class stud:
    count=0
    def __init__(self):
        self.students=[]
    def addstudent(self,RNO,Name,per):
        self.students.append([RNO,Name,per])
        stud.count+=1
    def __str__(self):
        return(str(self.students)+"No of students"+len(students))
class result(stud):
    def topper(self):
        tpr=0
        per=0
        L=len(self.students)
        for i in range(L):
            if (self.students[i][2]>per):
                tpr=i
                per=per.students[i][2]
        print("Topper"+self.students[tpr])
        
