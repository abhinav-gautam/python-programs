n= int(input())
a=[int(input()) for _ in range(n)]
maximum=a[0]
for i in range(len(a)):
    if maximum<a[i]:
        maximum=a[i]
print(maximum)
