


x=int(input())
matrix=[]
for i in range(x):
    matrix.append(list(map(int, input().rstrip().split())))
#print (matrix)

def difference(arr, x):
    d1 = 0
    d2 = 0
 
    for i in range(0, x):
        for j in range(0, x):
            if (i == j):
                d1 += arr[i][j]
            if (i == x - j - 1):
                d2 += arr[i][j]
    return abs(d1 - d2)

print(difference(matrix, x))