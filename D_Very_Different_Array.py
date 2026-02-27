for _ in range(int(input())):
    n, m = map(int, input().split())
    
    petya = list(map(int, input().split()))
    whole = list(map(int, input().split()))
    
    petya = [[num, i] for i, num in enumerate(petya)]
    
    sorted_petya = sorted(petya)
    whole.sort()
    
    brother = []
    
    iw, jw = 0, m - 1
    ip, jp = 0, n - 1
    
    while ip <= jp:
        left_pet, left_index = sorted_petya[ip]
        right_pet, right_index = sorted_petya[jp]
        
        left_whole = whole[iw]
        right_whole = whole[jw]
        
        l1, l2 = abs(left_whole - left_pet), abs(right_whole - left_pet)
        r1, r2 = abs(left_whole - right_pet), abs(right_whole - right_pet)
        
        if max(l1, l2) > max(r1, r2):
            if abs(left_whole - left_pet) > abs(right_whole - left_pet):
                brother.append([left_whole, left_index])
                iw += 1
            else:
                brother.append([right_whole, left_index])
                jw -= 1
            
            ip += 1
            
        else:
            if abs(left_whole - right_pet) > abs(right_whole - right_pet):
                brother.append([left_whole, right_index])
                iw += 1
            else:
                brother.append([right_whole, right_index])
                jw -= 1
            
            jp -= 1
    
    total = 0
    for num, index in brother:
        total += abs(num - petya[index][0])
    
    print(total)
    
    