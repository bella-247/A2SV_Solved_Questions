import sys

input = sys.stdin.readline

def solution():
    s = input().strip()
    t = input().strip()
    n = len(s)
    m = len(t)

    # Start index in s
    for i in range(n):
        # Turning point index in s
        for j in range(i, n):
            # 1. Build the rightward part
            # This is the substring from i up to j
            right_part = s[i:j+1]
            
            # If the current rightward movement doesn't even match the start of t, skip
            if not t.startswith(right_part):
                continue
            
            # 2. Build the leftward part
            # Remaining characters needed from t
            rem_len = m - len(right_part)
            
            # We turn left starting from j-1. We need rem_len characters.
            # So we take substring from s starting backwards from j-1
            # Ending at j-1 - rem_len
            left_part = ""
            current_pos = j - 1
            while len(left_part) < rem_len and current_pos >= 0:
                left_part += s[current_pos]
                current_pos -= 1
            
            # Check if total path matches t
            if right_part + left_part == t:
                print("YES")
                return

    print("NO")

def main():
    line = input().strip()
    if not line: return
    q = int(line)
    for _ in range(q):
        solution()

if __name__ == "__main__":
    main()