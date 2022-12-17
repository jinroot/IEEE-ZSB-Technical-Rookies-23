
def chocolateFeast(n, c, m):
    # Write your code here
    count=0
    wrappers=0
    count += int(n/c)
    wrappers += int(n/c)
    #print(wrappers,count)
    while(wrappers>=m):
        count += int(wrappers/m)
        temp=wrappers%m
        wrappers=temp+int(wrappers/m)
    return(count)





chocolateFeast(10,2,5)