# To calculate the sum of a particular series
print("To calculate the sum of (x)-(x^3)/(3!)+(x^5)/(5!)-(x^7)/(7!).......upto n terms : ")
x=int(input("Enter the value of x : "))
n=int(input("Enter the value of number of terms  : " ))
sum=0
fact=1
for i in range(1,n+1,1):
    fact=fact*(i*2-1)
    if i%2!=0:
        sum=sum+(x)**(i*2-1)/fact
    else:
        sum=sum-(x)**(i*2-1)/fact
    fact=fact*(i*2)
print("The sum of the given series is : ",sum)
print ("Developed by Abhinav Kumar Gautam")
