def giaithua(n):
    if(n==1):
        return 1
    return giaithua(n-1)*n
a = int(input("Nhap so: "))
print(giaithua(a))