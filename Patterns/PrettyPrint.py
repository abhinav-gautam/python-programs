a = 3
n = 2*a - 1
temp = [[a for _ in range(n)] for i in range((n//2)+1)]
main = [[a for _ in range(n)]]

for i in range(1, (n//2)+1):
    tempList = temp[i-1]
    for j in range(i, n-i):
        tempList[j] -= 1
    temp[i] = tempList
    main.append(tempList[:])

main.extend(reversed(main[0:-1]))
for i in range(len(main)):
    print(main[i])