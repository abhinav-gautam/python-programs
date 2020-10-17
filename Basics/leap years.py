# To display all the leap years of the 21st centuary
print("leap years of the 21stt centuary from 2010 to 2100 : ")
z=0
for i in range(2010,2101,1):
    if i%4==0:
        z=z+1
        if z<=10:
            print(i,end=" ")
        else:
            z=1
            print()
            print(i,end=" ")
print ("Developed by Abhinav Kumar Gautam")
