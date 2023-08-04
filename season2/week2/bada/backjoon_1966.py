'''
문제 : 1966번 프린터 큐
난이도 : 실버3

#1
우선순위 큐를 이용하면 되겠다!
파이썬에서 우선순위 큐는? -> heapq

#2
heapq는 우선순위가 오름차순, 내림차순으로 바꿀 순 없나?
-> 파이썬에는 최대 힙이 구현되어 있지 않기 때문에 내림차순 정렬을 위해서는 부호를 바꾼 뒤 최소 힙을 이용하면 된다.
-> https://velog.io/@janeljs/python-for-coding-test-6

#3
중요도가 높은 문서가 하나라도 있으면, queue의 가장 뒤에 재배치,,,
-> heapq말고 deque를 이용해보자
'''
from collections import deque
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    printer = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while printer:
        _max = max(printer)
        front = printer.popleft()
        m -= 1

        if _max == front:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            printer.append(front)
            if m < 0:
                m = len(printer) - 1