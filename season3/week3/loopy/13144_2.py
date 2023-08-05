# 13144 List of Unique Numbers
# https://www.acmicpc.net/problem/13144
# N^2
import sys

N = int(sys.stdin.readline())
arr = sys.stdin.readline().split()

p1 = 0
p2 = 0

count = 0

while(p1 != N or p2 != N):
    if not p1 == p2 and arr[p1] == arr[p2]:
        p2 = ++p1
        continue
    ++p2; ++count;
    if p2 == N: 
        p2 = ++p1

print(count)