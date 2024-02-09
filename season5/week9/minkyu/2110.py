import sys
input = sys.stdin.readline

N, C = list(map(int, input().split()))
wifi_list = []
for _ in range(N):
    wifi_list.append(int(input()))
wifi_list.sort()

start = 1
end = wifi_list[-1] - wifi_list[0]
answer = 0

while start <= end:
    now = wifi_list[0]
    cnt = 1
    mid = (start + end) // 2
    for i in range(1, N):
        if wifi_list[i] - now >= mid:
            cnt += 1
            now = wifi_list[i]
    if cnt >= C:
        if answer < mid:
            answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)
