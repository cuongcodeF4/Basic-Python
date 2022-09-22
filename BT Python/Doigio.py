t=int(input("Nhập giây muốn đổi:"))
H=(t//3600)%24
M=(t%3600)//60
S=(t%3600)%60
if H>=12:
    H=H-12
    print("{0}:{1}:{2}:PM".format(H,M,S))
else:
    print("{0}:{1}:{2}:AM".format(H,M,S))
