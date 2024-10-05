def xto5(x):
    strx=str(x)
    while int(strx)%5!=0:
        x=int(x)//10
        strx=str(x)
    return strx
import sys
sys.stdin=open('Bai1.INP',mode='r')
sys.stdout=open('Bai1.OUT',mode='w')
x=input()
so=''
for i in x:
    if i.isdigit():
        print(i,end='')
        so+=i
tam=''
t=0

for i in x:
    if i.isdigit():
        tam+=i
    else:
        if (i.isalpha() or (i=='' or i==' ')) and tam!='':
            t+=int(tam)
        tam=''
if (i.isalpha() or (i=='' or i==' ')) and tam!='':
    t+=int(tam)
t+=int(tam)

print()
print(xto5(so))
print()
print(t)
