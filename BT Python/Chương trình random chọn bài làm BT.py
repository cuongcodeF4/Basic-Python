import random
dem=0
print("Bài tram : 1")
print("Bài miền : 1")
print("Bài vẽ liên tục : 1")
print("Bài t : 1")
while True:
    a=randrange(2,5)
    b=randrange(2,5)
    c=randrange(2,5)
    if a!=b and b!=c and a!=c:
        print("Chương trình random làm bài thí nghiệm vật lí 1:")
        print("Chương:",a)
        print("Cường:",b)
        print("Chính:",c)
        dem+=1
        print("Số lần chạy là:",dem)
        exit()