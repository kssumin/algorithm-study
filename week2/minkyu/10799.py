from collections import deque

bar = deque(input())

count_left = 0
count_right = 0
count_laser = 0
count_bar = len(bar)
result = 0
is_laser1 = False
is_laser2 = False
while bar:
    op = bar.popleft()
    # 해당 문자가 (인지 )인지 구별하는 코드
    if op == '(':
        count_left += 1
        is_laser1 = True
    else:
        count_right += 1
        is_laser2 = True
    # op == ')'가 없으면 )(를 레이저로 인식해버린다
    if is_laser1 and is_laser2 and op == ')':
        count_laser += 1
        is_laser1 = False
        is_laser2 = False
        count_right -= 1
        count_left -= 1
        result += count_left
    else:
        # 레이저가 아닌데 )가 들어왔을 때는 괄호가 닫힐 때, 즉 선분이 끝나는 지점이다
        if op == ')':
            count_left -= 1
            count_right -= 1

# 답 = 막대기 + 막대기를 통과하는 레이저의 개수 인데 아래 코드는 막대기 개수를 더하는 코드이다
result += count_bar//2 - count_laser
print(result)

"""
코드로 작성하기 전에 일단 답이 어떻게 나오는지 알아봤다.
답을 구하려면 막대기의 개수와 각각의 막대기를 통과하는 레이저의 개수를 세서 더하면 된다.그냥 깡 레이저의 개수는 ()의 개수를 세고,
막대기의 개수는 len(bar)를 2로 나눈 다음 깡 레이저의 개수를 빼면 막대기의 개수가 나온다.
그래서 이걸 구현했는데 바로 전 문제를 큐로 풀어서 그런지 큐로 풀어야하는 줄 알고 큐로 풀었다..
큐로 풀었을 때 문제점이 하나씩 pop 을 하기 때문에 이미 pop 해버린 값을 알아내기가 어려워 ()가 레이저인지 구별하는 것이 힘들었다.
그래서 is_laser 라는 변수를 사용했다.
다 풀고 보니 스택으로 푸는게 훠어어어어엉ㄹ씬 나았을 것 같다.

풀이
일단 bar 를 읽으면서 (의 개수와 )의 개수를 센다. 그리고 (가 나오다가 )가 나오면 레이저로 인식한다. (가 연속해서 있을 때는
한 레이저를 지나는 선분이 여러 개 있음을 나타낸다. 따라서 ( 다음 )가 들어와서 레이저가 들어왔다고 인식하면 count_left - 1 만큼의 선분을 그 레이저가 지나간다.
그래서 result 에 count_left 값을 더해준다. 레이저로 인식하면 count_left 와 count_right 를 -1씩 해준다.
레이저가 아닌데 )가 들어왔다면 선분이 끝나는 지점이다. 따라서 count 를 -1씩 해준다.
각각의 막대기를 통과하는 레이저의 개수를 다 더했으니 마지막으로 막대기의 개수를 더해줬다.
"""
