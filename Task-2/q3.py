
word = "hello"
input = input()
i = 0
j = 0
while i < len(word) and j < len(input):
    if word[i] == input[j]:
        i += 1
    j += 1
if i == len(word):
    print("YES")
else:
    print("NO")
