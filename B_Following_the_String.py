from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    trace = list(map(int, input().split()))
    
    letters = set("abcdefghijklmnopqrstuvwxyz")
    dicts = defaultdict(list)
    s = []
    
    for num in trace:
        if num == 0:
            letter = letters.pop()
            dicts[num].append(letter)
            s.append(letter)
            
        else:
            need = num - 1
            letter = dicts[need].pop()
            dicts[num].append(letter)
            s.append(letter)

        
    print("".join(s))
        