# 가장 높은 것부터 비교해서

import sys; input = sys.stdin.readline
t = int(input())
for i in range(t):
    count = 1
    lst = []
    top = 0
    n = int(input())
    for j in range(n):
        docu, inte = map(int, input().split())
        lst.append((docu, inte))
    lst.sort(key=lambda x : x[0])
    for i in range(1, len(lst)):
        if lst[i][1] <= lst[top][1]:
            top = i
            count += 1
    print(count)
