# 请判断下列各组数是否可以构成无向图的度数列。
# （1）1 1 1 2 3 5 6 3
# （2）1 2 2 4 6 7 8 9

#  是否可以列出所有可能来进行判断？但这样太麻烦了哎呦
#  还需要考虑不是简单图的情况，比如：自己成环的情况以及平行（形成环）
#  可以先运用握手定理进行判断，是否可以进行
# 第一步：输入一组代表一个图（可能）的每个结点的度的序列
print("示例：")
print("1 1 1 2 3 5 6 3\n1 2 2 4 6 7 8 9\n0")
flag = 1
data = []
print("输入度数序列后，再输入0代表输入度数序列结束")
while flag == 1:
    temp = list(map(int, input('plz input your order:').split()))
    if 0 != temp[-1]:
        data.append(temp)
    else:
        flag = 0


# print(data)
# 第二步：进行判断
# 根据握手定理进行判断，握手定理：每个图中，结点度数的总和等于边数的两倍。

# 计算结点个数
def countnode(orderdata):
    length = []
    count = 0
    while count < len(orderdata):
        length.append(len(orderdata[count]))
        count += 1
    return length


# print(length)

def countside(orderdata):
    # 生成结点
    N = len(orderdata)
    nodedata = [chr(i) for i in range(97, 97 + N)]  # 定义结点“a b c d ...”
    print("定义结点为：a b c d ...")
    print(nodedata)
    sidedata = [('0', '0')]

    orderdata.sort(reverse=True)
    sidecount = [0 for h in range(N)]  # 定义一个数组，存储结点的连线个数

    for q in nodedata:
        num = 0  #
        count = 0  # 边数
        node = orderdata[nodedata.index(q)]  # 该节点应有边数
        # 先检查自己有几条边
        for j in sidedata:
            if j[0] == q or j[1] == q:
                count += 1
        for p in range(nodedata.index(q) + 1, len(nodedata)):
            #  p 从 q的后一个结点开始，到最后一个结束
            # 如果自己已有的边数等于node，向下查找
            if count == node:
                break
            elif count < node:
                sidedata.append((q, nodedata[p]))
                sidecount[nodedata.index(q)] += 1
                sidecount[nodedata.index(nodedata[p])] += 1
            else:  # count > node 一个结点已经连线的数目超过了可能应该连线的数目
                # 处理：断开这个结点与它连线的其中一个的连线，并让这个与他断开的结点与新的结点进行连线，但是这个需要符合要求
                cach = ''
                index = 0
                for f in sidedata:
                    if f[0] == q or f[1] == q:
                        cach = f[0]  # 重新连线的准备
                        index = sidedata.index(f)
                        del sidedata[sidedata.index(f)]  # 断开连线
                        sidecount[nodedata.index(q)] -= 1  # f
                        sidecount[nodedata.index(cach)] -= 1  # cach
                    # 重新连线 和一个符合要求的进行连线,当删除完连线后，进行连线
                    # 连线：sidecount 数组存储各个结点已经连线的数目
                    # 如果有的话，找一个连线数目不够，或者没有连线的结点
                    # 因为是判断出画出图，所以肯定可以找到
                    if sidecount[nodedata.index(q)] == node:
                        # 应该找几个0：原度数 - 现度数
                        for u in range(orderdata[nodedata.index(cach)] -
                                       sidecount[nodedata.index(cach)]):
                            for o in sidecount:
                                if o == 0:  # 只有是0才进行连线（只能是0）
                                    sidedata.insert(index, (cach, nodedata[sidecount.index(o)]))
                                    sidecount[nodedata.index(cach)] += 1
                                    break
                        # 在上面循环完后，已经完全重新连线了，需要结束循环
                        if orderdata[nodedata.index(cach)] - sidecount[nodedata.index(cach)] == 0:
                            break
            if sidecount[nodedata.index(q)] == node:
                break
    # print(sidecount)
    del sidedata[0]
    print("该度数列组成的无向图的一种连线方式：")
    for k in sidedata:
        print(f"{k[0]}->{k[1]}")


# countside(data)

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


# 选做：是否可以简单图化（前提是可以简单图化），通过Havel定理
#

def habelgraph(orderdata):

    data = [k for k in orderdata]
    cach = 0
    if 1 == graph(data):  # 首先要能够进行图化
        flag = True
        while flag:
            num = 0
            # 进行排序
            data.sort(reverse=True)
            if data[0] == 0:
                break
            # 删除第一个元素,并记录第一个数的值
            cach = data.pop(num)
            # 让后 cach 个数据 全都减1
            for i in range(cach):
                data[i] = data[i] - 1
                if data[i] == -1:
                    return 0
            num += 1

        if flag:
            return 1
    else:
        return 0


for i in data:
    if habelgraph(i) == 1:
        print(f"----------{[data.index(i) + 1]}----------")
        print(f"第{data.index(i) + 1}个可以组成简单图")
        countside(data[data.index(i)])
    else:
        print(f"----------{[data.index(i) + 1]}----------")
        print(f"第{data.index(i) + 1}个无法组成简单图")
