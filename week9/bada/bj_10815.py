'''
문제 : 숫자 카드 (10815)
난이도 : 실버5

숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

in 메서드는 list 자료형보다 set 자료형에서 더 빠르다는 게 생각나서 상근이가 가지고 있는 숫자 카드를 set으로 저장함
'''
import sys

n = int(sys.stdin.readline())
n_set = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

answer = []


for i in m_list:
    if i in n_set:
        answer.append(1)
    else:
        answer.append(0)

for a in answer:
    print(a, end=" ")
