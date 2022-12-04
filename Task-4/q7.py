
def groupAnagrams(strs):
    result = {}
    for i in strs:
        x = "".join(sorted(i))
        if x in result:
            result[x].append(i)
        else:
            result[x] = [i]
    return list(result.values())

lst = []
num=int(input())
for i in range(num):
    lst.append(input())

print(groupAnagrams(lst))