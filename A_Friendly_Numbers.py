def d(num):
    summ = 0
    while num > 0:
        summ += num % 10
        num //= 10

    return summ


maxx = 81
for _ in range(int(input())):
    x = int(input())
    count = 0
    for num in range(maxx):
        y = x + num
        if y - d(y) == x:
            count += 1
    
    print(count)
