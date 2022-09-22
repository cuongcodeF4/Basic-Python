
def F(n):
    if n==1 or n==2:
        return 1
    else:
        return F(n-2)+F(n-1)
def ListF(n):
    for i in range(1,n+1):
        print(F(i),end='\t')

n=int(input("Nhập ví trí thứ n của dãy Fibonacci:"))
print(ListF(n))
