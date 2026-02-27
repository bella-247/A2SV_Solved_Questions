n, m = list(map(int, input().split()))

arr1 = list(map(int, input().split()))

arr2 = list(map(int, input().split()))
result = []
i = j = 0
while i < n and j < m:
    if arr1[i] <= arr2[j]:
        result.append(arr1[i])
        i += 1
        
    else:
        result.append(arr2[j])
        j += 1
        

while i < n:
    result.append(arr1[i])
    i += 1    
    
while j < m:
    result.append(arr2[j])
    j += 1
    
print(*result)
