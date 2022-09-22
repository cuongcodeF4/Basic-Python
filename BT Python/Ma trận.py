from random import randrange

a2D=[]
dong=int(input("Nhập số dòng:"))
cot=int(input("Nhập số cot:"))
for i in range(dong):
    onedong=[]
    for j in range(cot):
        onedong.append(randrange(-100,100))
    a2D.append(onedong)
print("Ma trận do máy nhập là:")
for i in range(dong):
    for j in range(cot):
        print(a2D[i][j],end='\t')
    print()