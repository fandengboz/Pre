# 偏序关系的确定，通过矩阵进行判断
# 自反，反对称，传递性的确定
# 矩阵的输入
print("请输入矩阵的规模（示例：3）：3")
m = int(input("plz input a number:"))
print("输入示例：\n1 1 1\n1 1 0\n0 0 1")
data = []
flag = 0
while flag < m:
    temp = list(map(int, input("plz input a matrix:\n").split()))
    if len(temp) != m:
        continue
    if len(temp) == m:
        flag += 1
        data.append(temp)
print(data)


# （1）自反性的验证
def introspectmx(datamx):
    flag1 = 0
    for i in range(len(datamx)):
        if datamx[i][i] == 1:
            flag1 += 1
    if flag1 == m:
        return 1
    else:
        return 0


# print(introspectmx(data))


# (2)反对称性的验证
# 验证矩阵的转置矩阵，他们相同位置的元素的值应相同
def antisymmetrymx(datamx):
    Rc = []
    flag2 = 0
    for i in range(len(datamx)):
        CacheList2 = []
        for j in range(len(datamx)):
            CacheList2.append(datamx[j][i])
        Rc.append(CacheList2)
    # print(Rc)
    for k in range(m):
        for q in range(m):
            if datamx[k][q] == Rc[k][q]:
                flag2 += 1
    if flag2 != m * m:
        return 1  # 具有反对称性
    else:
        return 0


# print(antisymmetrymx(data))


# (3)验证传递性
# 计算出矩阵的传递矩阵，如果与原矩阵相同，则验证传递性
def transfermx(datamx):
    # 进行Warshall运算
    i = 0
    flag3 = 0
    datamxc = datamx
    while (i < m):
        for j in range(m):
            if datamx[j][i] == 1:
                for k in range(m):
                    datamx[j][k] = datamx[j][k] or datamx[i][k]
        i += 1
    # 验证矩阵是否相同
    for k in range(m):
        for q in range(m):
            if datamxc[k][q] == datamx[k][q]:
                flag3 += 1
    if flag3 != m * m:
        return 0
    else:
        return 1

# [[1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
# print(transfermx(data))

# 验证是否是偏序关系
if introspectmx(data) and antisymmetrymx(data) and transfermx(data) == 1:
    print("该矩阵是偏序关系")
else:
    print("该矩阵不是偏序关系")

