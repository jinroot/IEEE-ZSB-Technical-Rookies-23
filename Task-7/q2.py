stones = [2,7,4,1,8,1]

while(len(stones)>1):
    v1 = max(stones)
    n = stones.index(v1)
    del stones[n]
    v2 = max(stones)
    m = stones.index(v2)
    del stones[m]
    if v1 == v2:
        continue
    elif v1>v2:
        stones.append(v1-v2)

if len(stones)==0:
    print("0")
else:
    print(stones[0])