'''
/*문제 정보 */
2805번 - 나무 자르기
난이도 - 실버 2
/*풀이 방법 */
1부터 n 까지 도는 방식으로는 시간초과가 걸린다.
이분탐색으로 mid 의 값과 비교해 답을 구했다.
'''
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)
mid = 0

while start <= end:
    mid = (start + end) // 2
    ans = 0
    for i in tree:
        if i > mid:
           ans += (i - mid)
        if ans > m:
            break
    if ans >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
'''
/*오답 노트*/
오답1 : 시간초과
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
tree = list(map(int, input().split()))

cut_tree = 0
meter = max(tree)

while 1:
    meter -= 1
    for i in range(n):
        if tree[i] - meter >= 0:
            cut_tree += tree[i] - meter
    if cut_tree == m:
        print(meter)
        break
    cut_tree = 0
    
if tree[i] - meter >= 0:      
      cut_tree += tree[i] - meter
      if cut_tree > m:
        break
 나무를 더하는 과정에서 이미 m 을 넘으면 break 를 걸어줘도 시간초과

/*느낀 점*/
 if num >= m :
            break
 이분탐색이어도 이 if 문을 걸지 않으면 시간 초과가 걸렸다.
'''