s=[]
s=[i**2 for i in range(10)]
print(s)
a=[]
a=[x for x in s if x%2==0 ]
print(a)
d=[]
d=[x for x in s if x %2!=0]
print(d)
e=tuple(d)
print(e)
w=(d,e)
print(w)
for a in w:
    print(a)