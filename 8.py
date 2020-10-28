a = [1,3,4,5]
def printSeq():
    for i in a:
        print(i,end=" ")
    print()
    return
print("Hi there, this is our sequence:")
printSeq()
x = input("Where do you want to delete (head/tail): ")
if(x=="head"):
    a.pop(0)
elif(x=="tail"):
    a.pop()
else:
    print("error")
print("This is our new sequence: ")
printSeq()