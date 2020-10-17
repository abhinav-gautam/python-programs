import string
import sys
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr.reverse()
for i in range(0,len(arr)):
    print arr[i],
