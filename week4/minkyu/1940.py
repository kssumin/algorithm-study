import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

materials_list = list(map(int, input().split()))
materials_set = set(materials_list)
cnt = 0
for num in materials_list:
    first = num
    last = M - first
    if last in materials_set:
        cnt += 1

print(cnt//2)

"""
풀이
재료들은 고유한 번호를 가지고 있으므로 중복이 없다. 따라서 재료들을 set에 저장한 후 재료쌍을 찾아주면 된다.
하지만 이렇게 하면 /2를 해주어야 한다. 만약 4를 찾아야 하고 재료가 1,3이라면 1과 3에서 한번씩 cnt에서 더해버리니 /2를 해주어야한다.

처음 코드
처음 든 생각이 그냥 이중 for문 쓰면 될 거 같아서 했는데 시간초과가 났다.

materials = list(map(int, input().split()))
cnt = 0
for i in range(len(materials)-1):
    first = materials[i]
    for j in range(i+1, len(materials)):
        last = materials[j]
        if first + last == M:
            cnt += 1
"""