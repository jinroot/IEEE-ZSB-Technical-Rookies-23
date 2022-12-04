def rotate90Clockwise(matrix):
    N = len(matrix[0])
    K= N-1
    for i in range(N // 2):
        for j in range(i, K - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[K - j][i]
            matrix[K - j][i] = matrix[K- i][K - j]
            matrix[K - i][K - j] = matrix[j][K - i]
            matrix[j][K - i] = temp

def printmatrix(matrix):
    N = len(matrix[0])
    for i in range(N):
        print(matrix[i])
 

x=int(input())
matrix=[]
for i in range(x):
    matrix.append(list(map(int, input().rstrip().split())))
rotate90Clockwise(matrix)
printmatrix (matrix)

