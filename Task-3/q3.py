
inp = int(input())
totalWater = 0
bottles=[]
for i in range(0,inp):
    info = input().split()
    totalWater += int(info[0])
    bottles.append(int(info[1]))

bottles.sort()
maxCap = bottles[len(bottles)-1]+bottles[len(bottles)-2]
#print(maxCap,totalWater)
if maxCap > totalWater:
    print("Yes")
else:
    print("No")