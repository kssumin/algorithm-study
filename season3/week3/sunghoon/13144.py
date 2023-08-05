'''
/*문제 정보 */
13144번 - List Of Unique Numbers
난이도 - 골드 4
/*풀이 방법 */
https://velog.io/@kakasi18/Two-Pointers-Boj13144-List-of-Unique-Numbers
리뷰했습니다.
투포인터 문제 풀이
'''
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

count = [0] * 100001

r = -1
answer = 0
sum = 0

for l in range(n):
    while r +1 < n and count[nums[r+1]] == 0:
        r += 1
        count[nums[r]] += 1
        sum += 1

    answer += sum
    sum -= 1
    count[nums[l]] -= 1

print(answer)


'''
/*오답 노트*/
/*느낀 점*/
처음 이 문제를 봤을 때, 큐나 덱으로 풀어야지만 생각했지 투포인터는 절대
생각 못했었다... 아마 이 문제를 발표 주제로 하지 않을까 싶다..!
'''