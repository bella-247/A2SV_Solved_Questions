for _ in range(int(input())):
    s = input()
    n = len(s)
    
    if "**" in s or ">*" in s or "*<" in s or "><" in s:
        print(-1)
        continue
    
    left_count = s.count("<")
    right_count = s.count(">")
    random_count = s.count("*")

    print(max(left_count, right_count) + random_count)