class student():
    no_of_student=0
    teacher_name="Sir"
    def __init__(self,studName,per):
        self.studName=studName
        self.per=per
        student.no_of_student+=1
        self.grade=""
    def calgrade(self):
        if(self.per>=90 and self.per<100):
            self.grade="A+"
        elif(self.per>=80 and self.per<89):
            self.grade="A"
        elif(self.per>=70 and self.per<79):
            self.grade="B"
        elif(self.per>=60 and self.per<69):
            self.grade="C"
        elif(self.per>=50 and self.per<59):
            self.grade="D"
        else:
            self.grade="Fail"
        print("Student grade is ",str(self.grade))
    
            
        
