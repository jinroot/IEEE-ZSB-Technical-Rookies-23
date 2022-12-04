word1 = input()
word2 = input()
found = False
count = 0
for i in range(len(word2)):
    if(word1.count(word2[i])>0):
        count+=1
        if(count == len(word1)):
            found = True
            break
    else:
        count = 0
if(found):
    print("true")
else:
    print("false")