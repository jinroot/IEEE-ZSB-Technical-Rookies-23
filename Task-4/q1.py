inp = input().split()
n1 = int(inp[0])
k = int(inp[1])
arr = input().split()
for i in range(n1):
    arr[i] = int(arr[i])
arrCount = [0]*(max(arr) + 1)
for i in arr:
    arrCount[i]+=1
for i in range(k):
    print(arrCount.index(max(arrCount)),end=" ")
    arrCount[arrCount.index(max(arrCount))] = 0