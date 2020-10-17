obw=open("C:\Users\ssv74\Desktop\Sample.txt","w")
n=int(input("Enter no of students"))
for i in range(n):
    rno=raw_input("Enter roll no")
    name=raw_input("Enter name")
    per=raw_input("Enter per")
    obw.writelines(rno+" "+name+" "+per+'\n')
obw.close()
obr=open("C:\Users\ssv74\Desktop\Sample.txt","r")
n=int(input("Enter no of students"))
for i in range(n):
    print(obr.readlines(n))
