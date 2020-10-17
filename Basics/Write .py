def write(n):
    obw=open("F:\My Projects\students.txt","w")
    obw.writelines("Roll no   Name    Percentage"+'\n')
    for i in range(n):
        rn=raw_input("Enter roll no")
        name=raw_input("Enter name")
        per=raw_input("Enter percentage")    
        obw.writelines(rn+"         "+name+"          "+per+'\n')    
    obw.close()
def read():
    obr=open("F:\My Projects\students.txt","r")
    for i in range(n):
        line=obr.readline()
        print line
n=int(input("Enter no of students"))
write(n)
read()
