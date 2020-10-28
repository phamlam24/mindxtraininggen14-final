a = [1,5,1,5,4,21,-12,4,-11,431,-44,1,0]
l = 13
def findMin(currentMin,pos):
    if(pos==l):
        return currentMin
    if(a[pos]<currentMin):
        return findMin(a[pos],pos+1)
    else:
        return findMin(currentMin,pos+1)
print(findMin(999999999999,0))