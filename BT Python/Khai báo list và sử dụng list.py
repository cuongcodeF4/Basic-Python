a=[1,5,7]
b=a
b[1]=0
a.insert(0,999)
del a[1:3]
print(b)
print(a)