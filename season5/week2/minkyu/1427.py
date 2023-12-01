import sys
input = sys.stdin.readline

N = list(input().rstrip())
N.sort(reverse=True)
N = "".join(N)
print(N)