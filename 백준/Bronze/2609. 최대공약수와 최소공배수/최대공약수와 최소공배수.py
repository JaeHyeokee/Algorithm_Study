def gcd(a, b):
    if a % b == 0: return b
    else: return gcd(b, a % b)
def lcm(a, b): return int(a * b / gcd(a, b))
a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))