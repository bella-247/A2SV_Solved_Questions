s = input()

word = "hello"

i = 0
for j in range(len(s)):
    if i < len(word) and word[i] == s[j]:
        i += 1
        
        
print("YES" if i == len(word) else "NO")