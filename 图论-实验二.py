# 1.给出邻接矩阵，判断是否是连通图

# 直接判断是否具有传递性就好

# 矩阵的输入：
# print("请输入矩阵的规模（示例：4）：")
# m = int(input("plz input a number:"))


# print("请输入矩阵：")
# print("示例：\n0 1 1 1\n1 0 1 0\n1 1 0 1\n1 0 1 0")
data = [[0, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0]]

'''
flag = 0
while flag < m:
    temp = list(map(int, input("plz input a matrix:\n").split()))
    if len(temp) != m:
        continue
    if len(temp) == m:
        flag += 1
        data.append(temp)
'''


# 判断是否是无向图 : 度数为奇数的结点的个数是偶数
def graph(orderdata):
    num = 0
    count = 0
    for i in orderdata:
        count += i
    for j in orderdata:
        if j % 2 != 0:
            num += 1
    if num % 2 == 0 and count % 2 == 0:
        return 1
    else:
        return 0


# graph(data)
# 判断是否具有连通性，采用深度优先算法dfs

def dfs(datamx, visited, num):
    length = len(datamx)
    visited[num] = True
    for j in range(length):  # j 是列 ，进行遍历
        # 找可以走的路
        if datamx[num][j] == 1 and not visited[j]:
            dfs(datamx, visited, j)


def isConnect(data):
    visited = [False for _ in range(len(data))]
    dfs(data, visited, 0)
    for k in visited:
        if not k:
            return False
    return True


# 判断是否是欧拉图，具有一条欧拉回路，才是欧拉图
def euler(datamx):
    length = len(datamx)
    flag = False
    nodecount = []
    for i in datamx:
        nodecount.append(i.count(1))
    # 首先：连通
    if isConnect(datamx):
        if 1 == graph(nodecount):
            # 具有欧拉回路：结点度数全为偶数
            for j in nodecount:
                if j % 2 != 0:
                    return 0
    return 1


# 如果是一个欧拉图，输出一个欧拉回路,采用弗罗莱(Fluery)算法
def nodecreate(datamx):
    N = len(datamx)
    node = []
    nodedata = [chr(i) for i in range(97, 97 + N)]
    for i in range(N):
        cachnode = []
        for j in range(N):
            if data[i][j] == 1:
                cachnode.append(nodedata[j])
        node.append(cachnode)
    return node, nodedata


# 判断是否是连通图，不包括这条边以及之前已经走过的边
def isBridge(num, i):
    index = nodedata.index(i)  # i 的位置
    # 移除这条边
    data[num][index] = 0
    data[index][num] = 0
    # 检查是否是连通图
    visited = [False for _ in range(len(data))]
    dfs(data, visited, 0)

    for l in visited:
        if not l:
            data[num][index] = 1
            data[index][num] = 1
            return False

    data[num][index] = 1
    data[index][num] = 1
    return True


def eulergraph(num):
    for i in node[num]:
        if isBridge(num, i):  # True :不是桥， False:是桥
            print(f"{nodedata[num]}->{i}", end=" ")
            node[nodedata.index(i)].remove(nodedata[num])
            node[num].remove(i)
            eulergraph(nodedata.index(i))


# ----------------主函数-----------------------
# （1）（2）
print("题目矩阵：")
print("0 1 1 1\n1 0 1 0\n1 1 0 1\n1 0 1 0")
print("----------[1]----------")
datar = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
if isConnect(datar):
    print("这是一个无向连通图")
else:
    print("这不是一个无向连通图")
print("----------[2]----------")
if 1 == euler(datar):
    print("这是一个无向欧拉图")
else:
    print("这不是一个无向欧拉图")
# （3）
print("----------[3]----------")
print("实验用矩阵：")
print("0 1 0 0 1 0 0 0\n1 0 1 0 0 0 0 0\n0 1 0 1 0 0 0 0\n0 0 1 0 1 1 0 0\n1 0 0 1 0 0 0 1\n0 0 0 1 0 0 1 0\n0 0 0 0 0 1 0 1\n0 0 0 0 1 0 1 0")
N = len(data)
node, nodedata = nodecreate(data)
print("举例结点为：a,b,c,d....")
print(nodedata)
if 1 == euler(data):  # 结点全为偶数
    # 进行欧拉回路的查找
    num = 0  # # 选取顶点为起点
    eulergraph(num)

else:  # 有两个奇数结点
    nodecount = []
    count1 = 0
    count2 = 0
    index = 0
    for i in data:
        nodecount.append(i.count(1))
    for k in nodecount:
        if k % 2 != 0:
            index = k
            count1 += 1
        else:
            count2 += 1
    if count1 == 2 and count2 == len(data) - 2:
        eulergraph(index)
