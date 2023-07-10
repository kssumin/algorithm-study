'''
/*문제 정보 */
12865번 - 평범한 베낭
난이도 - 골드 5
/*풀이 방법 */
냅색 알고리즘으로 풀었다.
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
item = [[0, 0]]
knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for _ in range(n):
    item.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = item[i][0]
        value = item[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[n][k])
'''
/*오답 노트*/
/*느낀 점*/

'''