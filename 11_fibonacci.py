def fibonacci(t):
    if(t==1 or t==2):
        return 1
    return fibonacci(t-1) + fibonacci(t-2)

x = [0,1,1]
def fibonacci_optimized(t):
    for i in range(3,t+1):
        x.append(x[i-1] + x[i-2])
    return x[t]
a = int(input("nhap so: "))
print(fibonacci(a))
print(fibonacci_optimized(a))