import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)
num_list.sort()
# num_list[0]값과 num_list[-1]이 같으면 continue 되기 때문에 마지막에 INF 값 추가
num_list.append(INF)
result = 0
length = len(num_list) - 1
for i in range(length):
    if num_list[i] == num_list[i-1]:
        continue
    else:
        result = max(result, num_list[i] * (length - i))

print(result)
"""
풀이
입력값들을 작은 순으로 정렬한 다음 첫 번째 로프부터 들 수 있는 무게를 계산한다.
같은 숫자가 연속해서 나오면 계산할 필요가 없으므로 continue 한다
첫 번째 풀이
왜 이리 쉽지 하면서 풀었는데 틀렸다.
그냥 입력값의 최솟값 * N을 했는데 반례가 있다.
N이 3이고 입력값이 10 20 20 이면 로프를 두 개만 써서 40을 들어올릴 수 있지만
내 코드는 30을 출력한다.
'로프를 전부 사용하지 않아도 된다'라는 조건을 안 보고 풀었다.
N = int(input())
num_set = set()
for i in range(N):
    num = int(input())
    num_set.add(num)
print(min(num_set) * N)
"""