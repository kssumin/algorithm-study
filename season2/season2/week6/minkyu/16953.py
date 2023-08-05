import sys
input = sys.stdin.readline

A, B = map(int, input().split())
result = 0
is_correct = False

def dfs(num):
    global result, is_correct
    if num == A:
        is_correct = True
        result += 1
        return
    if num % 2 == 0:
        result += 1
        dfs(num // 2)
    elif str(num)[-1] == '1':
        if num == 1:
            return
        result += 1
        dfs(int(str(num)[:-1]))


dfs(B)
if is_correct:
    print(result)
else:
    print(-1)
"""
풀이
dfs로 푼다고 풀었던 거 같은데 dfs가 아닌 것 같다. 아닌가 맞나 헷갈린다.
반대로 하는게 더 편할 거 같아서 B를 A로 바꾸는 걸 택했다.
조건을 거꾸로 하면 2로 나누어지면 2로 나누고, 1이 끝자리에 있으면 제거하면 된다.
2로 나눠지면서 끝자리에 1이 있는 경우가 없으니 계산하기 더 편하다.
위 조건들 둘 다 할 수 없다면 연산을 더 할 수 없다는 뜻이니 연산할 수 없을 때의 숫자가 A거나 연산 도중 A와 같다면 몇 번 연산했는지 출력한다. 
"""