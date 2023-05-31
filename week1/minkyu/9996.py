import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
crash_file_name = list(input().rstrip())

for _ in range(N):
    file_name = deque(list(input().rstrip()))
    queue = deque(crash_file_name)
    while file_name:
        if len(queue) == 1:
            print("DA")
            break
        if queue[0] != '*':
            left = queue.popleft()
            if left != file_name[0]:
                print("NE")
                break
            file_name.popleft()
        if queue[-1] != '*' and file_name:
            right = queue.pop()
            if right != file_name[-1]:
                print("NE")
                break
            file_name.pop()
    else:
        if len(queue) != 1:
            print("NE")
        else:
            print("DA")

"""
풀이
투포인터 알고리즘을 썼다.
왼쪽과 오른쪽을 차례로 비교했다.

21번째줄에 and file_name을 작성하기 전에는 인덱스에러가 떴었다.
만약 입력으로 아래 값이 들어온다면
1
abc*def
a
file_name은 왼쪽부터 탐색할 때 a가 같으니 빈리스트로 바뀐다.
그럼 오른쪽도 탐색하기 위해서 22번째줄 아래로 코드가 진행하게 되는데 오른쪽 문자가 맞는지 탐색할 때
빈 리스트에서 pop할 수 없어서 인덱스 에러가 떴었다.
while문 조건에 빈 리스트는 탐색하지 못하게 한 줄 알았는데 아니었다.
"""