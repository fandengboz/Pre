#面向结果
Box1 = Box2 = Box3 = 1
A = not Box1
B = not Box2
C = not B
if(not A):
    #说明BC是错的，发生值的改变
    B1 = not B
    C1 = not C
    #值改变之后他们应该都是1，进行判断
    result = A and B1 and C1
    if(result):
        print("在第一个箱子里")
if(not B):
    A2 = not A
    C2 = not C
    result = A2 and B and C2
    if(result):
            print("在第二个箱子里")
if(C):
    A3 = not A
    B3 = not B
    result = A3 and B3 and C
    if(result):
        if(A3):
            print("在第一个箱子里")
        else:
            print("在第三个箱子里")
                  
















    