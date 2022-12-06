x = int(input())
i = 2
list= []
while(i <= x **(1/2)):
    while(x%i == 0):
        list.append(i)
        x = x /i
    i += 1

list.append(int(x))
print(*list)