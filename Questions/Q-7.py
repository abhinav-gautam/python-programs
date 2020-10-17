class Society:
    def __init__(self,society_name="Surya Apartments",house_no=20,no_of_members=3,flat="A Type",income=25000):
        self.society_name=society_name
        self.house_no=house_no
        self.no_of_members=no_of_members
        self.flat=flat
        self.income=income
    def inputdata(self):
        self.society_name=raw_input("Enter Society Name")
        self.house_no=int(input("Enter house no"))
        self.no_of_members=int(input("Enter no of members"))
        self.flat=raw_input("Enter flat type")
        self.income=float(input("Enter income"))
    def allocate_flat(self):
        if self.income>=25000:
            self.flat="A Type"
        elif self.income>=20000 and self.income<25000:
            self.flat="B Type"
        elif self.income>15000 and self.income<20000:
             self.flat="C Type"
        else:
            self.flat="D Type"
    def Showdata(self):
         print "Society Name",self.society_name
         print "House Number",self.house_no
         print "Number of members",self.no_of_members
         print "Flat Type",self.flat
         print "Income",self.income
a=Society()
a.inputdata()
a.allocate_flat()
a.Showdata()


            
