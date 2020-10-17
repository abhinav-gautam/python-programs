#day of the week.
q=int(input("Enter the day of the month : "))
m=int(input("Enter the month : "))
k=int(input("Enter the year : "))
j=(k/100)
h=(q+(26*((m+1)/10))+k+(k/4)+(j/4)+(5*j))%7
if h<1:
    print("day is Saturday.")
elif 1<h<2:
    print("day is sunday.")
elif 2<h<3:
    print("day is monday.")
elif 3<h<4:
    print("day is tuesday.")
elif 4<h<5:
    print("day is wednesday.")
elif 5<h<6:
    print("day is thursday.")
elif 6<h<7:
    print("day is friday.")
else:
    print("not found.")
print ("Developed by Abhinav Kumar Gautam")
