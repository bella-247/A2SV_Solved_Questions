s = input()
vasya = ""
word = {"h" : 1, "e" : 1, "l" : 2, "o" : 1}

for c in s:
    if c not in word or word[c] == 0:
        continue
    else:
        vasya += c
        word[c] -= 1
        
if vasya == "hello":
    print("YES")

else:
    print("NO")
