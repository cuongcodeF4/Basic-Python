from random import randrange
print("Bài miền        : 1 ,2và 4")
print("Bài khối        : 3 ,5và 6")
while True:
    a = randrange(1, 4)
    b = randrange(1, 4)
    c = randrange(1, 4)
    d = randrange(4, 7)
    e = randrange(4, 7)
    f = randrange(4, 7)
    if a!=b and b!=c and a!=c and a!=d and a!=e and a!=f and b!=d and b!=e and b!= f and c!=d and c!=e and c!=f and d!=e and d!=f and e!=f:
        print("Chương trình random làm bài mỹ thuật trong công nghiệp:")
        print("Huy:",a)
        print("Cường:",b)
        print("Chính:",c)
        print("Thắng:", d)
        print("Trí:", e)
        print("Ngọc:", f)