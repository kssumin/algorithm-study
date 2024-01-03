def dfs():
    if len(tmp)>=M:
        numbers.append(list(tmp))
    
    else:
        for i in range(1,M+1):
            tmp.append(i)
            dfs()
            tmp.pop()

N,M = map(int, input().split())
tmp = []
numbers = []

dfs()

for i in numbers:
    print(i)