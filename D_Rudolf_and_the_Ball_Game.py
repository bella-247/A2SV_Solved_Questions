import sys

input = sys.stdin.readline

def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def rs():
    return input().strip()

def ri():
    return int(rs())

def rls(spliter=" "):
    return list(map(int, rs().split(spliter)))

def solution(_):
    n, m, x = rls()
    x -= 1  # Convert to 0-indexed

    # We maintain a set of current possible positions
    possible_positions = {x}

    for _ in range(m):
        throw_str, direction = rs().split()
        throw = int(throw_str)
        next_positions = set()

        for pos in possible_positions:
            if direction == "0" or direction == "?":
                # Clockwise
                next_positions.add((pos + throw) % n)
            if direction == "1" or direction == "?":
                # Counter-clockwise
                next_positions.add((pos - throw) % n)
        
        possible_positions = next_positions

    # Convert back to 1-indexed, sort, and print
    result = sorted(pos + 1 for pos in possible_positions)
    print(len(result))
    print(*result)

def main():
    t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()