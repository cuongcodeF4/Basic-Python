'''def sum1(n):
    s=0
    while n> 0:
        s+=1
        n-=1
    return s
def sum2():
    global val
    s=0
    while val >0:
        s+=1
        val-=1
    return s
def  sum3():
    s=0
    for i in range(val,0,-1):
        s+=1
        return s
def main():
    global val
    val=5
    print(sum2())
    print(sum1(5))
    print(sum3())

main()'''
'''def oscillate():
    for i in range(-3,5):
        print(i,end='')
        print(-i,end='  ')
print(oscillate())'''
'Hàm tính tổng ước số'
def TongUS(n):
    global s
    s=0
    for i in range(1,n):
        if n%i==0 :
            s=s+i
    return print("Tổng ước số của",n,"là:",s)
n=int(input("Tính tổng ước số của :"))
print(TongUS(n))
def checkperfectnumber(n):
    if s == n :
        return print("Số",n," là số hoàn thiện")
    return print("Số",n," không phải là số hoàn thiện")
print(checkperfectnumber(n))
def checkAbuntdantnumber(n):
    if s>n:
        return print("Số",n,"là số thịnh vượng")
    return print("Số",n,"không phải là số thịnh vượng")
print(checkAbuntdantnumber(n))


