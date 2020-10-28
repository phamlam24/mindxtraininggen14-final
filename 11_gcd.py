def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

x = int(input("nhap so thu nhat: "))
y = int(input("nhap so thu hai: "))
print(gcd(x,y))