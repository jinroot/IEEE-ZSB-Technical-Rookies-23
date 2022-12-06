
def maxHeap(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] > A[k]:
        maximum = l
    else:
        maximum = k
    if r < len(A) and A[r] > A[maximum]:
        maximum = r
    if maximum != k:
        A[k], A[maximum] = A[maximum], A[k]
        maxHeap(A, maximum)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_max_heap(input):
    n = int((len(input)//2)-1)
    for k in range(n, -1, -1):
        maxHeap(input,k)


string = input().split()
list = list()
for i in range(len(string)):
   list.append(int(string[i])) 

build_max_heap(list)
print(list)