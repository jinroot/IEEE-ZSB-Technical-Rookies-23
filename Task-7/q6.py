def kaprekarNumbers(p, q):
    # Write your code here
    arr=[]
    for i in range(p,q+1):
        n=str(i*i)
        k=len(n)
        left=slice(0,k//2)
        right=slice(k//2,k)
        #print(n[left],n[right])
        if n[left] and n[right] and int(n[left])+int(n[right])==i or i == 1:
            arr.append(i)

    if not arr:
        print('INVALID RANGE')
    else:
        for i in arr:
            print(i,end=" ")

 
 
 
p = int(input().strip())
q = int(input().strip())
kaprekarNumbers(p, q)