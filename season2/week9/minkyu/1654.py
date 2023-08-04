import sys
input = sys.stdin.readline

K, N = map(int, input().split())
num_list = []
for i in range(K):
    num_list.append(int(input()))
start, end = 0, sum(num_list) // N
while end >= start:
    mid = (start + end) // 2
    if mid == 0:
        print(1)
        exit(0)
    result = 0
    for num in num_list:
        result += num // mid
    if result >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
"""
2805번이랑 똑같이 풀었더니 풀렸다.
end값은 (랜선들의 합 / 랜선 개수)보다 클 수 없으니 end 값을 랜선들의 합 // 랜선 개수로 한다. 
"""
