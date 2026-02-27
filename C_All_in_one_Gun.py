def bestOrder(n, bullets):
    i = 0
    for j in range(n - 1, -1, -1):
        if j <= i:
            break
        
        if bullets[i] >= bullets[j]:
            i += 1
            
        else:
            bullets[i], bullets[j] = bullets[j], bullets[i]

def minSeconds(bullets, n, h, k):
    seconds = 0
    
    i = 0
    while h > 0:
        h -= bullets[i]
        i = (i + 1) % n
        seconds += 1
        
        if i - 1 == -1 and h > 0:
            seconds += k
            
    return seconds

for _ in range(int(input())):
    n, h, k = list(map(int, input().split()))
    bullets = list(map(int, input().split()))
    
    bestOrder(n, bullets)

    print(minSeconds(bullets, n, h, k))