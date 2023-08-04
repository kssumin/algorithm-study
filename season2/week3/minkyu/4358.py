import sys
input = sys.stdin.readline

total = 0
tree_dict = {}
while 1:
    tree_name = input().rstrip()
    if not tree_name:
        break
    total += 1
    tree_dict.setdefault(tree_name, 0)
    tree_dict[tree_name] += 1

tree_dict = sorted(tree_dict.items())

for tree, count in tree_dict:
    print("{} {:.4f}".format(tree, count/total*100))

"""
1. 처음에 EOF 를 잘못 다뤄서 계속 시간초과가 났다. 

2. total += 1을 if not tree_name: 위에 써서 틀렸다고 나왔다. 나무 종류가 들어왔을 때 total 이 증가해야 하는데
그냥 while 문이 돌자마자 +1을 해서 틀렸다.

3. 11번째 줄에 setdefault 를 1로 해서 틀렸었다. 

풀이
저번 문제랑 비슷하다. 저번 문제처럼 dict 에 저장하고 key 순으로 정렬해서 출력했다. 
"""