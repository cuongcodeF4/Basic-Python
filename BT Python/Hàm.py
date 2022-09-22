def BCNN(a,b):
    'Hàm dùng để tìm bội chung nhỏ nhất của 2 số'
    if a >b:
        max=a
    else:
        max=b
    for i in range(max,(a*b)+1,1):
        if i%a ==0 and i% b == 0 :
             return print("Bội chung nhỏ nhất của ", a, "và", b, "là:",i)
BCNN(5,7)
print(BCNN)










