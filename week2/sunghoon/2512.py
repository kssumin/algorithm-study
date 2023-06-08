'''
/*문제 정보 */
2512번 - 예산
난이도 - 실버 3
/*풀이 방법 */
이분탐색으로 상한액을 구해서 출력 나오게 했다.
'''
import sys
input = sys.stdin.readline

def zzz(start, end):
    while start <= end:
        count = 0
        mid = (start + end) // 2

        for i in arr:
            count += min(i, mid)

        if count <= m:
            start = mid + 1
        else:
            end = mid - 1
    return end


n = int(input())
arr = list(map(int, input().split()))
m = int(input())

print(zzz(0, max(arr)))
'''
/*오답 노트*/
오답 1.
import sys
input = sys.stdin.readline

n = int(input())
l = sorted(list(map(int, input().split())))
m = int(input())

if sum(l) <= m:
    print(max(l))

else:
    result = m
    for i in range(n):
        result -= l[i]
        if result < 0:
            result += l[i]
            result += l[i-1]
            print(result // (n-i + 1))
            
진짜 주제를 생각하는게 너무 어려워서 그냥 무지성으로 작성했다. 출력 초과가 나왔다.
/*느낀 점*/
이분탐색을 풀 때 마다 느끼는 것은 머릿속에선 이해가 되지만 적용할 때 마다 이게 된다는게 이해가
잘 되지 않는다..
'''