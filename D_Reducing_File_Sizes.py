def minimumCompressions(files, n, m):
    # sum of the compressed
    if sum(file[1] for file in files) > m:
       return -1
    
    files.sort(key=lambda file: file[0] - file[1], reverse=True)
    total_sum = sum(file[0] for file in files)
    
    i = 0
    while i < n and total_sum > m:
        total_sum -= (files[i][0] - files[i][1])
        i += 1
        
    return i


n, m = list(map(int, input().split()))
files = [list(map(int, input().split())) for _ in range(n)]

print(minimumCompressions(files, n, m))