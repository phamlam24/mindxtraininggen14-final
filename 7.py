a = [1,3,4,5]
def printSeq():
    for i in a:
        print(i,end=" ")
    print()
    return
print("Hi there, this is our sequence:")
printSeq()
x = int(input("What do you want to add: "))
a.insert(0,x)
print("This is our new sequence: ")
printSeq()