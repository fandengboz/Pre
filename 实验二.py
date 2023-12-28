print("选择的是第一个式子")
YS = []
print("p\tq\t-r\tY\t")
for p in range(2):
    for q in range(2):
        for r in range(2):
            f_r = int (not r)
            result =int( p and (q or (not r)))
            YS.append(result)
            print(f"{p}\t{q}\t{f_r}\t{result}\t")
print("\n")
count = 0
for i in range(len(YS)) :
    count = YS[i] + count
if(count == 0):
    print("矛盾式")
if(count == len(YS)):
    print("重言式")
else:
    print("可满足式")
    
        