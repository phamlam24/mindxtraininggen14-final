import math
def quadro(a,b,c):
    delta = b*b-4*a*c
    if(delta>0):
        return [(-b+math.sqrt(delta)/(2*a)),(-b-math.sqrt(delta)/(2*a))]
    elif(delta==0):
        return [-b/2/a]
    else:
        return []

print(quadro(1,4,3))
print(quadro(2,8,8))
print(quadro(-99.131,1,-1))