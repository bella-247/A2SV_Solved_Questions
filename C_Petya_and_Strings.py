a = input()
b = input()

lower_a = a.lower()
lower_b = b.lower()

if lower_a == lower_b:
    print(0)

elif lower_a < lower_b:
    print(-1)
    
else:
    print(1)