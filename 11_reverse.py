def int_reverse(ans,cur):
    if(cur==0):
        return ans
    ans = ans * 10+(cur%10)
    cur = cur//10
    return int_reverse(ans,cur)
a = int(input("Nhap so: "))
print(int_reverse(0,a))