import sys

input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    ptr = 1
    results = []
    
    for _ in range(t):
        n = int(data[ptr])
        ptr += 1
        # Sort and take unique values to speed up the check
        a = sorted(list(set(map(int, data[ptr : ptr + n]))))
        ptr += n
        
        num_unique = len(a)
        if num_unique <= 3:
            results.append("0")
            continue
            
        def check(mid):
            # Carvers can cover a range of 2 * mid
            count = 1
            # First carver starts at a[0] and covers up to a[0] + 2*mid
            limit = a[0] + 2 * mid
            
            for i in range(1, num_unique):
                if a[i] > limit:
                    count += 1
                    if count > 3:
                        return False
                    limit = a[i] + 2 * mid
            return True

        # Binary search for the minimum waiting time
        low = 0
        high = 10**9
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        results.append(str(ans))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()