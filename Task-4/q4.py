def addOne(lst,index):
    if(lst[index]==9):
        lst[index]=0
        return addOne(lst,index-1)
    else:
        lst[index]+=1

size=int(input())
lst=[0]
lst = list(map(int,input().split()))
lst.insert(0,0)
addOne(lst,len(lst)-1)
if(lst[0]==0):
    del lst[0]
for i in range(1,len(lst)):
    print(lst[i],end=" ")
