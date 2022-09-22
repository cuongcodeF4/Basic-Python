import math

try:
    r=float(input("Nhập bán kính của đường tròn:"))
    Dt=math.pi*r**2
    print("Diện tích của đường tròn là:",Dt)
    Cv=2*math.pi*r
    print("Chu vi của đường tròn là:",Cv)
except:
    print("Đã bị lỗi!!!")