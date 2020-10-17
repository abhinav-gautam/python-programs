ps='Rungta'
rs='Sankara'
x=open('C:\Users\ssv74\Desktop\p.txt',"r")
f1=x.read()
x.close()
y=open('C:\Users\ssv74\Desktop\Story.txt',"w")
y.writelines(f1)
y.close()
a=open('C:\Users\ssv74\Desktop\Story.txt',"r")
z=a.read()
w=z.split(' ')
for i in range(len(w)):
    if (w[i]==ps):
        w[i]=rs
a.close()
b=open('C:\Users\ssv74\Desktop\Story.txt',"w")
b.writelines(w)
b.close()



    
