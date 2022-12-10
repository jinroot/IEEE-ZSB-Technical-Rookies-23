def hackerrankInString(s):
    # Write your code here
    word = 'hackerrank'
    n = len(word)
    for i in range(len(s) - 1, -1, -1):
        if word[n - 1] == s[i]:
            n -= 1
        if n == 0:
            return "YES"
    if i == 0:
        return "NO"