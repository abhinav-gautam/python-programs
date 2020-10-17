ob=open("C:\Users\ssv74\Desktop\p.txt","r")
content=ob.read()
words=content.split(' ')
for i in range(len(words)-1,-1,-1):
    print words[i],

