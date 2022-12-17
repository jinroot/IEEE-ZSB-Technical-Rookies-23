

r1=[int(k) for k in input().split()]
r2=[int(k) for k in input().split()]
r3=[int(k) for k in input().split()]

arr= [["1","1","1"],["1","1","1"],["1","1","1"]]

ls= [r1,r2,r3]
for i in range(3):
    for j in range(3):
        for k in range(ls[i][j]):
            up = i - 1
            right = j + 1
            down = i + 1
            left = j - 1            
            if arr[i][j] == "0":
              arr[i][j]="1"
            else:
                arr[i][j]="0"
            if(up in [0,1,2]):
                if arr[up][j] == "0":
                  arr[up][j]="1"
                else:
                    arr[up][j]="0"
            if(left in [0,1,2]):
                if arr[i][left] == "0":
                  arr[i][left]="1"
                else:
                    arr[i][left]="0"
            if(right in [0,1,2]):
                if arr[i][right] == "0":
                  arr[i][right]="1"
                else:
                    arr[i][right]="0"
            if(down in [0,1,2]):
             if arr[down][j] == "0":
               arr[down][j]="1"
             else:
                 arr[down][j]="0"
for i in range(3):
    print(arr[i])