def circularArrayRotation(a, k, queries):
    # Write your code here
    ans = [0]*len(a)
    for i in range(len(a)):
        temp = (i + k)%len(a)
        ans[temp] = a[i]
    output = []  
    for i in queries:
        output.append(ans[i])
        print(ans[i])
    return output


circularArrayRotation([3, 1, 9,2,5,1,5], 8, [0,1,2,3,4])