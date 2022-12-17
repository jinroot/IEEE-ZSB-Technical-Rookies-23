
n = int(input())

while(True):
    n +=1
    ls=list(str(n))
    if len(ls) == len(set(ls)):
        break

print(n)