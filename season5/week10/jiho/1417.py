# 표 가장 많은 사람부터 정렬시킨다. (다솜씨를 제외한 나머지)
# 그렇다면 다솜씨가 기호 1번이니깐 먼저 하게 하면 되겠네
import sys; input = sys.stdin.readline

lst = []
cnt = 0
peoples = int(input())
dasom = int(input())
for i in range(peoples - 1):
    lst.append(int(input().rstrip()))
lst.sort(reverse=True)

if peoples == 1: # 단일 후보라면
    print(0)
else:
    while lst[0] >= dasom:
        dasom += 1
        lst[0] -= 1
        cnt += 1
        lst.sort(reverse=True)
    print(cnt)

