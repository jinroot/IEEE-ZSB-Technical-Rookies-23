input = input()
ls=list(input)
ans=''
while(len(ls) != 0):
    if ls[0]=='.':
        ans += '0'
        del ls[0]
    elif ls[0]+ls[1]=='-.':
        ans += '1'
        del ls[0]
        del ls[0]
    elif ls[0]+ls[1]=='--':
        ans += '2'
        del ls[0]
        del ls[0]
print(ans)

