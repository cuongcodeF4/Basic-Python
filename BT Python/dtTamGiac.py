from math import *

while True:
    print("                              CHƯƠNG TRÌNH TÍNH DIỆN TÍCH TAM GIÁC")
    a=float(input("Nhập chiều dài cạnh a="))
    b=float(input("Nhập chiều dài cạnh b="))
    c=float(input("Nhập chiều dài cạnh c="))
    if a<=0 or b<=0 or c<= 0 or a+b <= c or a+c<=b or b+c<=c :
        print("Error, lỗi nhập số")
        print("MỜi bạn nhập lại")
    else:
        break
p=(a+b+c)/2
dt=sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích của tam giác là S=",dt)


