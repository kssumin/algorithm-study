import sys; input = sys.stdin.readline

cnt1, cnt2 = map(int, input().split())
router = []
for i in range(cnt1):
    router.append(int(input().rstrip()))
router.sort()

def binary_search(router, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = router[0]
        cnt = 1

        for i in range(1, len(router)):
            if router[i] >= current + mid:
                cnt += 1
                current = router[i]
        if cnt >= cnt2:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

start = 1
end = router[-1] - router[0]
answer = 0
binary_search(router, start, end)

print(answer)
