ob=open("C:\p.txt","r")
a=ob.read()
line=a.split("\n")
words=[]
wordsl=[]
for i in range(len(line)):
    word=line[i].split(" ")
    wordsl.append(word)
    for i in range(len(word)):
        if word[i]=="":
            pass
        else:
            words.append(word[i].lower())
n=len(words)
def remove_duplicates(words):
    c=0
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            if words[i]==words[j]:
                words[j]=0
                c=1
        c=0
    return(words)
words=remove_duplicates(words)
wordsu=[]
for i in range(n):
    if words[i]!=0:
        wordsu.append(words[i])
c=0
print "Words------Line no"
for i in range(len(wordsu)):
    print wordsu[i],"------",
    for j in range(len(wordsl)):
        for k in range(len(wordsl[j])):
            if wordsu[i].lower()==wordsl[j][k].lower():
                c=1+j
        if c!=0:
            print c,
            c=0
        else:
            pass
    print    
            
