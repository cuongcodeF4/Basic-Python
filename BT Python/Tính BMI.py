def BMI(kg,h):
     return kg/(h**2)
def phanloai(bmi):
    if bmi <=18.5:
        return "Gầy"
    elif bmi <= 24.9:
        return"Bình thường"
    elif bmi <= 29.9 :
        return "Hơi béo"
    elif bmi <=34.9 :
        return "Béo phì cấp độ 1"
    elif bmi <= 39.9:
        return "Béo phì cấp độ 2"
    else:
        return " Béo phì cấp độ 3"
print("Nhập cân nặng của bạn:")
kg=float(input())
h=float(input("Nhập chiều cao của bạn:"))
bmi=BMI(kg,h)
print("BMI của bạn:",bmi)
print(phanloai(bmi))