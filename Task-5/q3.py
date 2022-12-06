
def valid(input):
    lst = []
    while True:
        input = sum(int(i) ** 2 for i in str(input))
        if input == 1 or input in lst:
            #print(input)
            break
        else:
            #print(input)
            lst.append(input)
    return input


input = int(input())
test = valid(input)
if test == 1:
    print("true")
else:
    print("false")