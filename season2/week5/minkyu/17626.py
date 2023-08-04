import sys
input = sys.stdin.readline


def dp():
    for i in range(1, n + 1):
        if graph[i] == 0:
            result_set = set()
            tmp = int(i**(1/2))
            while tmp > 0:
                result = 1 + graph[i - tmp**2]
                if result == 2:
                    graph[i] = 2
                    break
                result_set.add(result)
                tmp -= 1
            if graph[i] and result_set == 0:
                graph[i] = min(result_set)
    return


n = int(input())
graph = [0] * (n + 1)
root = int(n**(1/2))
for i in range(1, root + 1):
    graph[i**2] = 1

dp()
print(graph[n])
"""
풀이
pypy로 제출하니 바로 풀렸다... 2번째 풀이도 성공이네...
2번째 풀이에서 시간을 줄인 것 말고는 같다. 2번째 풀이를 봐주세용
첫 번째 풀이
그냥 입력 받은 숫자에서 가장 가까운 제곱수를 빼고 또 그 숫자에서 가까운 제곱수를 빼고 반복했다.
이렇게 풀면 12 = 9 + 1 + 1 + 1 --> 4가 나오는데
답은 12 = 4 + 4 + 4 --> 3이다.
이렇게 풀면 안될듯
tmp = int(n**(1/2))
result = 0
while 1:
    if tmp < 1:
        break
    if n - (tmp**2) >= 0:
        n -= tmp**2
        result += 1
    tmp -= 1
print(result)
두 번째 풀이
dp로 풀었는데 항상 min(tmp_list)를 계산해야해서 시간이 많이 걸리는 것 같다.
일단 graph에 제곱수는 1로 초기화하고 나머지는 0으로 초기화한다.
그리고 for문을 돌면서 1부터 n까지 graph에 0인 값들은 제곱수가 아니므로 몇 개의 제곱수로 이루어졌는지 계산하는 코드를 작성했다.
tmp에 int(i**(1/2))를 할당하고 tmp_list에 1 + graph[i - tmp] 값을 저장한다. tmp가 1이 될 때까지 tmp를 1씩 빼가면서 전 과정을 반복한다.
그 중 최솟값이 최소 개수로 만든 것이니 graph[i] = min(tmp_list)를 해준다.
def dp():
    for i in range(1, n + 1):
        if graph[i] != 0:
            pass
        else:
            tmp_list = []
            tmp = int(i**(1/2))
            while tmp > 0:
                tmp_list.append(graph[tmp**2] + graph[i - tmp**2])
                tmp -= 1
            graph[i] = min(tmp_list)
    return
n = int(input())
graph = [0] * (n + 1)
root = int(n**(1/2))
for i in range(1, root + 1):
    graph[i**2] = 1
dp()
print(graph[n])
세 번째 풀이
tmp가 int(i**(1/2)인 경우와 그 숫자에 1을 뺀 값으로만 계산했더니 틀렸다.
반례를 찾아보니
내 코드로는 48 = 36 + 12 --> 4, 25 + 24 -- > 4, min(4, 4) == 4로 틀렸다.
    답은   48 = 16 + 32 --> 3이 나와야한다. 
def dp():
    for i in range(1, n + 1):
        if graph[i] != 0:
            pass
        else:
            tmp = int(i**(1/2))
            num1 = graph[tmp**2] + graph[i - tmp**2]
            num2 = MAX
            if tmp > 1:
                tmp -= 1
                num2 = graph[tmp**2] + graph[i - tmp**2]
            graph[i] = min(num1, num2)
    return
네 번째 풀이
틀리고 나니 반례들이 많이 생각난다.
예를 들어 162 = 81 + 81 로 2가 답인데 내 코드는 3이 나온다.
두 번째 코드를 활용해서 코드를 다시 작성해야될듯
def dp():
    for i in range(1, n + 1):
        if graph[i] == 0:
            tmp = int(i**(1/2))
            num1 = i - tmp**2
            if graph[num1] == 1:
                graph[i] = 2
                continue
            elif graph[num1] == 2:
                graph[i] = 3
                continue
            else:
                graph[i] = 4
                while tmp > 1:
                    tmp -= 1
                    num1 = i - tmp**2
                    if graph[num1] == 2:
                        graph[i] = 3
                        break
    return
n = int(input())
graph = [0] * (n + 1)
graph[2], graph[3] = 2, 3
root = int(n**(1/2))
for i in range(1, root + 1):
    graph[i**2] = 1
dp()
print(graph[n])
"""