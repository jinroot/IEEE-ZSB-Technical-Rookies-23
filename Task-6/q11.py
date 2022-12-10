


time=0
days=0
x = input().split()
n = int(x[0])
t = int(x[1])


arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])
    time += 86400 - arr[i]
    days += 1
    
    if(time>=t ):
        print(days)
        break
        