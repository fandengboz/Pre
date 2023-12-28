
# 输入R关系后，全部转化为矩阵进行运算
List = []
data = []
temp = ()
# 步骤一：输入X集合
print("shuru输入")
print("输入示例：a b c d")
# 输入X集合
print("输入X集合:")
List = list(map(str, input().split(' ')))
# 展示输入结果
print(List)
# 步骤二：输入R关系
print("输入示例：\na b\nb a\nb c\nc d\n...")
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
# 展示输入结果
# print(data)
# 步骤三：转化为矩阵，使用01表示，采用布尔运算
length = len(List)
# 创建矩阵 length * length == 创建一个二维列表
M0 = [[0 for i in range(length)] for j in range(length)]
# 展示输入结果
# print(M0)
# 更改初始矩阵
for z in range(length):  # 0 1 2 3
    flag1 = 0  # 计数器，在迭代完一个序偶后，就结束循环，避免出现重复迭代同一个序偶的情况
    for j in List:  # 'a','b','c','d'
        if data[z][0] == j:
            for i in List:  # 'a','b','c','d'
                if data[z][1] == i:
                    M0[List.index(j)][List.index(i)] = 1
                    flag1 += 1
                    break
            if flag1 == 1:
                break


# print(M0)
# 根据矩阵，得出相应的序偶
# 输入想要转化的矩阵
def ordered_pair(*data):
    flag2 = 0
    list = []
    count = 0  # 记录行数
    for k in data:
        for z in k:  # z = 0,1,0,0
            for l in range(length):
                if z[l] == 1:
                    print(f"<{List[count]},{List[l]}>\t", end=" ")
            count += 1


print("输出原始序偶:")
ordered_pair(M0)

# 步骤三：进行关系闭包的运算
# （1）自反闭包
# 直接生成对角线为1的矩阵，再与原矩阵 进行or运算
M1 = []


def Judge(i, j):
    if j == i:
        return 1
    else:
        return 0


def introspect(*M0):
    diagonalList = [[Judge(i, j) for i in range(length)] for j in range(length)]
    # 展示输入结果
    # print(diagonalList)
    # 进行矩阵的逻辑加
    M1 = [[M0[i][j] or diagonalList[i][j] for j in range(length)] for i in range(length)]
    print("\n输出序偶的自反闭包：")
    # 得到相应序偶
    # print(M1)
    ordered_pair(M1)


introspect(*M0)
# (2)对称闭包
# 生成相应的转置矩阵（Rc矩阵）
Rc = []
for i in range(len(M0)):
    CacheList2 = []
    for j in range(len(M0)):
        CacheList2.append(M0[j][i])
    Rc.append(CacheList2)
# print(Rc)
MR2 = [[M0[i][j] or Rc[i][j] for j in range(length)] for i in range(length)]
# print(MR2)
print("\n输出序偶的对称闭包：")
ordered_pair(MR2)
# (3)Warshall算法-传递闭包
N = len(M0)
# 进行Warshall运算
i = 0
while (i < N):
    for j in range(length):
        if M0[j][i] == 1:
            for k in range(N):
                M0[j][k] = M0[j][k] or M0[i][k]
    i += 1
print("\n输出序偶的传递闭包：")
print(M0)
ordered_pair(M0)
