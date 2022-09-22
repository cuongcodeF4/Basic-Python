from math import log

print("Tính log cơ số a của x")
a=int(input("Nhập cơ số a="))
x=int(input("Nhập x="))
if a>0 and x>0 and a!=1 :
    t=log(x)/log(a)
    print("log cơ số a của x là:",t)
else:
    print("số không hợp lệ")