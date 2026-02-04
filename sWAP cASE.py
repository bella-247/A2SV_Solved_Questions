def swap_case(s):
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                s[i] = s[i].lower()
            else:
                s[i] = s[i].upper()
    
    return "".join(s)
