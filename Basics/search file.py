c=raw_input("Enter location of txt file to read")
obr=open(c,"r")
line=obr.read()
a=line.split(" ")
b=line.split(".")
print line
c=0
for i in range(len (a)):
    if a[i][:1] in ['a','e','i','o','u','A','E','I','O','U']:
        c=c+1
print 'No of words that begin with vowels are',c
print 'No of words that begin with consonants are',len(a)-c
print "No of lines are",len(b)
print "No of words are",len(a)

