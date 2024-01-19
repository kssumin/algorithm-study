import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num_list = list(map(int, input().split()))
start = 0
end = start + K
result = sum(num_list[start:end])
result_list = [result]
for i in range(N-K):
    result_list.append(result_list[i] - num_list[start+i] + num_list[end+i])
print(max(result_list))