

def sortNum(number):
    number = str(number)
    number = ''.join(sorted(number))
    number = int(number)
    return number

def sortNum2(number):
    number = str(number)
    number = ''.join(sorted(number,reverse=True))
    number = int(number)
    return number

inp = input()
counter = 0

while inp != '6174':
    y = sortNum(inp)
    z = sortNum2(inp)
    res = z - y
    if len(str(res)) < 4:
        inp = '0'*(4 - len(str(res))) + str(res)
    else:
        inp = str(res)
    counter += 1

print(counter)