'''
/*문제 정보 */
13164번 - 행복 유치원
난이도 - 골드 5
/*풀이 방법 */
아이들이 정렬되어 있는 것을 이용해 옆 사람과의 키차이를 구해 정답을 구했다.
키차이 정렬에서 k, 조가 하나씩 늘 때마다, 키차이 정렬 원소 중 하나를 뺄 수
있는 것이다. 문제예제에서 키차이 정렬이 2,2,1,4 인데 k =1 이면 2+2+1+4
k = 2 면 2+2+1, k=3 이면 2+1 이런 식으로 정답을 구할 수 있었다.
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
people = list(map(int, input().split()))

l = []
for i in range(1, n):
    a = people[i] - people[i-1]
    l.append(a)

l.sort()
result = 0

for j in range(n-k):
    result += l[j]

print(result)
'''
/*오답 노트*/
1.n, k = map(int, input().split())
people = list(map(int, input().split()))
group

for i in range(k):
    group[0][i].append
처음에는 무작정 그룹에서 가장 작은 애, 큰 애를 다른 조로 보내고 시작하려 했다.
/*느낀 점*/
난이도에 비해 쉬웠다.
'''