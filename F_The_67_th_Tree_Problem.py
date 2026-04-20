def solve():
    n = x + y
    if y == 0:
        print("NO")
        return
    
    # Parity check: The root's parity is fixed by x+y
    root_is_even = (n % 2 == 0)
    if root_is_even and x == 0:
        print("NO")
        return
    if not root_is_even and y == 0:
        print("NO")
        return

    print("YES")
    # Construction logic:
    # 1. Create a backbone of 'even' nodes by pairing them with 'odd' nodes.
    # 2. Attach remaining 'odd' nodes to the root.
    # (Specific edge printing logic follows...)