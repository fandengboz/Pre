# 1 转化为矩阵
List = []
data = []
temp = ()
# 步骤一：
print("输入A集合:")
print("输入示例：2 3 5 7 14 15 21")
# 输入A集合
List1 = list(map(str, input().split(' ')))
# 输入B集合
print("输入B集合:")
print("输入示例：2 7 3 21 14")
List2 = list(map(str, input().split(' ')))
# 展示输入结果
# print(List1)
# print(List2)
# 步骤二：输入R关系
print("输入示例：\n2 14\t3 15\t3 21\t5 15\n7 14\t7 21\t2 2 \t3 3 \n5 5 \t14 14\t15 15\t21 21")
# 控制循环结束
flag = 1
# 循环输入
while flag:
    temp = tuple(map(str, input("plz input R:(#作为结束标志):\n").split()))
    if temp == ():
        continue
    if temp != ('#',):
        data.append(temp)
    else:
        flag = 0
# 展示输入结果，R偏序关系
# print(data)


# 2 判断极大元，极小元
def covb(datamx):
    # 确定B的唯一盖住关系
    cov = []
    for j in datamx:  # 关系R中的元素
        flag2 = 0
        if j[0] != j[1]:  # x != y,j[0] = x, j[1] = y
            # 没有z，使得x偏序z，并且z偏序y
            for i in datamx:
                if j[0] == i[0]:  # i[0] = x ?
                    if i[1] != j[1]:  # i[1] 相当于 z， z != y ?
                        for k in datamx:
                            if i[1] == k[0]:  # z是否在偏序关系中存在？ if存在
                                if k[1] != j[1]:  # if z不偏序y
                                    flag2 += 1
                                    # 还没有遍历完震整个偏序关系，不应该直接加入，可能这个偏序的后面会有z存在
                                    # 可以加一个flag，遍历完i后进行flag的判断
            if flag2 != 0:
                cov.append((j[0], j[1]))
    # (2,14) (3,15)
    # print("盖住关系展示：")
    # print(cov)
    return cov


# 确定极大元
def ext(B, covdata):
    cachlevel = []
    ext = []
    for i in covdata:
        if int(i[0]) < int(i[1]):
            if cachlevel.count(i[1]) == 0:
                cachlevel.append(i[1])
    for j in covdata:
        for k in cachlevel:
            if k == j[0]:
                if int(j[0]) < int(j[1]):
                    cachlevel[cachlevel.index(k)] = j[1]
    for q in cachlevel:
        for p in B:
            if q == p:
                ext.append(p)
    print("这是极大元集合：")
    print(ext)


def tiny(B, covdata):
    cachlevel = []
    tin = []
    for i in covdata:
        if int(i[0]) < int(i[1]):
            if cachlevel.count(i[0]) == 0:
                cachlevel.append(i[0])
    for j in covdata:
        for k in cachlevel:
            if k == j[0]:
                if int(j[0]) < int(j[1]):
                    cachlevel[cachlevel.index(k)] = j[0]
    for q in cachlevel:
        for p in B:
            if q == p:
                tin.append(p)
    print("这是极小元集合：")
    print(tin)


ext(List2, covb(data))
tiny(List2, covb(data))

