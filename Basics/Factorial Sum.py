# Input 10 numbers and find the sum of their factorials
import time

begin = time.time()
def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
sum = 0
for i in range(10):
    num = int(input())
    sum += factorial(num)
print(sum)
end = time.time()
print(end-begin)

# Input 10 numbers and find the sum of their factorials in linear time
begin = time.time()
arr = [int(input()) for _ in range(10)]
factorial_arr = [1, 1]
sum = 0
for i in range(2, max(arr) + 1):
    factorial_arr.append(i*factorial_arr[i-1])
for x in arr:
    sum += factorial_arr[x]
print(sum)
end = time.time()
print(end-begin)
