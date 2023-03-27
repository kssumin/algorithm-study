'''
문제 : 저울 (2437)
난이도 : 골드 2

#1
정말 모르겠어서 다른 사람의 풀이를 봤다! 코드는 안 보고 아이디어만 봤습니당

이 문제의 핵심 : 측정할 수 있는 무게의 구간을 끊기지 않게 확장하는 것

Q) 현재 무게 0에서 10까지 측정할 수 있을 때, 무게 5의 추가 더 주어진다면 측정할 수 있는 구간은 어떻게 될까?
A) 
현재 측정 가능 구간 : [0, 10] ... (a)
추가적으로 측정 가능한 구간 : [0 + 5, 10 + 5] = [5, 15] ... (n)
최종 측정 가능 구간 : [0, 10] ... (c)

(a)와 (b)가 겹치기 때문에 측정할 수 있는 무게의 구간 (c)가 끊기지 않게 확장되었다.

만약 더 주어진 추의 무게가 15라면,
(b)가 [15, 25]가 되어버리기 때문에
(c)는 [0, 10], [15, 25]로 측정할 수 있는 무게의 구간이 끊겨버린다.

이렇게 되면 정답값은 10이 된다.
'''
import sys

n = int(sys.stdin.readline())
weights = sorted(list(map(int, sys.stdin.readline().split())))

acc = 0
for w in weights:
    if w <= acc + 1:
        acc += w
    else:
        break
print(acc + 1)

'''
오답
#1
import sys

n = int(sys.stdin.readline())
weights = sorted(list(map(int, sys.stdin.readline().split())))

acc = 0
for w in weights:
    if w <= acc + 1:
        acc += w
    else:
        print(acc + 1)
        break
마지막까지 구간이 끊기지 않으면 측정하지 못하는 최솟값은 모든 추의 합 + 1인데,
print를 for문 안에서 하니까 이 경우에는 답을 출력하지 못한다!

'''