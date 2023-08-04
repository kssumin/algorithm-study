'''
문제 : 암기왕 (2776)
난이도 : 실버 4

+
파이썬 in 연산자 시간복잡도
list, tuple에서 in 연산은 O(n)
set, dict에서 in 연산은 O(1)

이분 탐색 구현하는 것보다 set으로 입력받아서 in 연산하는게 더 빠른 것 같다.
이분 탐색 : O(nlogn)

#1
수첩 1의 내용을 입력받아 set에 저장
수첩 2를 순회하며 in 연산을 통해 값이 수첩 1에 존재하는지 확인
-> Good
'''
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    note1 = set(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    for i in list(map(int, sys.stdin.readline().split())):
        if i in note1:
            print(1)
        else:
            print(0)
