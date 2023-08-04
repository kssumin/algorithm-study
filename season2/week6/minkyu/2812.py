import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = input().rstrip()
count = 0
result = [num[0]]
for i in range(1, len(num)):
    while result:
        if result[-1] < num[i] and count < K:
            result.pop()
            count += 1
        else:
            break
    result.append(num[i])
# count가 K만큼 도달하지 못했을 때는 같은 숫자가 여러 개여서 삭제가 안된 경우
# ex) 22122인데 2번 제거해야하는 경우 1만 제거하고 2222에서 더 이상 제거하지 않는다.
if K != count:
    while count < K:
        result.pop()
        count += 1
print("".join(result))

"""
풀이
숫자가 들어오면 리스트에 저장한 뒤, for문을 돌면서 result에 저장한다.
for문을 돌 때 result에 있는 숫자보다 지금 숫자가 더 크다면 result에 있는 숫자를 차례로 제거한다.
count가 K가 될 때까지 제거한다.
만약 for문을 다 돌았는데 count가 K미만이라면 같은 숫자가 여러 개 있어 숫자 제거가 안된 것이니
제거가 안된만큼 result에서 제거한 후 출력한다.

"""
