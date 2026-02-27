n = int(input())
books = [list(map(int, input().split())) for _ in range(n)]

books[0][1] = max(books[0])

for i in range(1, n):
    book = books[i]
    
    if books[i][1] > books[i - 1][1] and books[i][0] > books[i - 1][1]:
        print("NO")
        break
    
    if max(books[i]) <= books[i - 1][1]:
        books[i][1] = max(books[i])
        
    else:
        books[i][1] = min(books[i])
        
else:
    print("YES")