def sumD(n):
    r=0
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    return (s)

# To find the sum of digits of a number
print("This programme is to find te sum of the digits of a number : ")
n=int(input("Enter the number : "))
s=sumD(n)
print("The sum of digits of the number ",n," is : ",s)
print ("Developed by Abhinav Kumar Gautam")
