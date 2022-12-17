
n = int(input())
arr = []
names=[]
print(arr,n)
for _ in range(n):
    name = input()
    score = float(input())
    arr.append([score,name])

arr.sort(key = lambda K: K[0])
m=arr[0][0]
print(m)
list(filter(lambda a: a != m, arr))
for i in range(len(arr)-1):
    if arr[i][0] == arr[i+1][0]:
        names.append(arr[i][1])  
        names.append(arr[i+1][1])
mynames = set(names)
print(mynames)
"""
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""