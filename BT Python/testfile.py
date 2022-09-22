from BTRL import *
while True:
    MSSP=input("Nhập mã sản phẩm:")
    TSP=input("Nhập tên sp:")
    GIA=float(input("Nhập đơn giá sp:"))
    line=MSSP+';'+TSP+';'+str(GIA)
    luudulieusp("databaese.txt",line)
    hoi=input("Có tiếp không(c/k)")
    if hoi=="k":
        exit()


