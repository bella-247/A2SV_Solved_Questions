t = int(input())
        
for _ in range(t):
    n = int(input())
    a = input().split()
    s = ""
    
    for word in a:
        if word + s < s + word:
            s = word + s
        else:
            s += word
    
    print(s)
    