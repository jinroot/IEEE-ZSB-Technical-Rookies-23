


bookPages=int(input("number of pages: "))
pageNum=int(input("page to seek: "))
answer =0
if pageNum <= bookPages/2:
    n=(pageNum-1)/2
    answer =int(-1 * n // 1 * -1)
elif pageNum > bookPages/2:
    while(True):
        bookPages -= 2
        answer += 1
        if bookPages <= pageNum:
            break

print(int(answer))