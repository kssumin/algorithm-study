import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())
for i in range(q):
    letter, start, end = input().rstrip().split()
    start = int(start)
    end = int(end)

    print(s[start:end+1].count(letter))
