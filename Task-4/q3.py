lst = input().split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
diff = len(lst)
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if (lst[i] == lst[j] and j - i <diff):
            diff = j - i
print(diff)