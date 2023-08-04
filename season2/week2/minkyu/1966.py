from collections import deque
import sys
input = sys.stdin.readline


def printer():
    M, N = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    index = N
    result = 0

    while 1:
        # 왼쪽의 있는 숫자의 출력 가능성을 판별하기 위해 pop
        is_print = queue.popleft()
        index -= 1
        if not queue and index == -1:
            result += 1
            print(result)
            break
        if is_print >= max(queue):
            result += 1
            if index == -1:
                print(result)
                break
        else:
            if index == -1:
                index = len(queue)
            queue.append(is_print)


R = int(input())
for i in range(R):
    printer()

"""
처음에 든 생각 : 오잉 그냥 중요도 큰 순서대로 출력하니깐 우선순위 큐에다가 -붙여서 하면되지 않나?
했는데 마지막 조건을 보고 못 쓰게 막았구나 생각했다. 우선순위 큐를 쓰면 중복값이 있을 때 몇 번째에 출력되는지 알아내지 못한다.
따라서 이 문제는 중요도만 생각하면 되는게 아니라 내가 찾으려는 데이터가 몇 번째에 있는지 계속 찾아내는게 중요하다.
 
그래서 처음엔 일단 내가 찾는 데이터의 순번을 index 에 저장하고 차례대로 왼쪽부터 그 숫자가 출력할만한지 알아내는 코드를 짜봤다.
처음 코드를 짰을 때는 
        if is_print >= max(queue):
            result += 1
            if index == 0:
                print(result)
                break
        else:
            if index == 0:
                index = len(queue)
            queue.append(is_print)
이런 식으로 짰었는데 잘못된 점이 세 개 있다....
1. 42번째 줄에서 'queue 의 가장 왼쪽에 있는 숫자가 제일 크면 result 에 1을 더하고 또 그 숫자의 인덱스가 0이면 몇 번째인지 출력한다'
처럼 보이는데 사실 인덱스가 -1일때로 바꿔주어야 한다. 왜냐면 내가 짠 코드는 index 에 -1을 pop 과 동시에 해버리기 때문에 
내가 찾고 있는 숫자의 출력 가능성을 따질 때는 pop 한 다음 index 에 -1을 한 상태이기 때문이다.
2. 이 코드는 내가 출력 순번이 궁금한 숫자가 젤 왼쪽에 있었는데 중요도가 가장 크지 않아서 append 를 해주어야 할 때 index 값을 대입하는 코드다.
그래서 마찬가지로 48번째 줄에서도 if index == -1:로 바꿔줘야한다. 
3. 또 숫자가 하나 들어올 때나 queue 에 숫자가 하나 남았을 때는 그 숫자를 pop 하고 그 숫자의 출력 가능성을 판별하려고 max 함수를 쓰는데
queue 에 값이 하나 들어왔는데 그 하나를 빼버리니 max 를 할 수 없었다. 그래서 16~19번째 줄을 추가했다. 지금 보니깐 index == -1 조건은 필요없었다...

풀이를 쓰면서 생각해보니 pop 하기 전에 max 값을 찾아서 변수에 대입해놓고 pop 한 숫자가 max 값보다 크거나 같다고 했으면 3번이 필요없었겠다.
이번에는 제출하기 전에 반례나 오류를 다 찾아서 그래도 한번에 정답이였다!

풀이
queue 에 처음 입력값을 저장해준다. 그리고 내가 궁금한 프린트의 index 를 저장하고 왼쪽부터 pop 해서 그 값이 출력할만한지 알아낸다.
출력할만한지 판별하기 전에 만약 queue 에 출력할 것이 더 없으면 무조건 프린트해야하기 때문에 프린트해준다.
pop 한 값이 프린트 목록 중에서 중요도가 가장 크면 출력한다. 그런데 pop 한 값이 우리가 찾는 값이였으면 result 를 출력하고 마친다.
출력하지 않는다면 그 값을 다시 queue 에 넣어준다. 
"""