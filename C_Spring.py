from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().split())
def read_list(): return list(map(int, input().split()))
def yn(res): print("YES" if res else "NO")

inf = float('inf')
MOD = 10**9 + 7

def solution(_):
    a, b, c, m = read_ints()
    alice_bob_lcm = (a * b) // math.gcd(a,b)
    bob_carol_lcm = (b * c) // math.gcd(b,c)
    alice_carol_lcm = (a * c) // math.gcd(a, c)
    alice_bob_carol_ = (alice_bob_lcm * c) // math.gcd(alice_bob_lcm, c)
    
    alice = (m // a) * 6
    bob = (m // b) * 6
    carol = (m // c) * 6
    
    alice_and_bob = (m // alice_bob_lcm) * 3
    alice -= alice_and_bob
    bob -= alice_and_bob
    
    bob_and_carol = (m // bob_carol_lcm)* 3
    bob -= bob_and_carol
    carol -= bob_and_carol
    
    alice_and_carol = (m // alice_carol_lcm) * 3
    alice -= alice_and_carol
    carol -= alice_and_carol
    
    alice_bob_and_carol = (m // alice_bob_carol_) * 2
                           
    alice += alice_bob_and_carol
    bob += alice_bob_and_carol
    carol += alice_bob_and_carol
    
    
    print(alice, bob, carol)
    
    


































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()