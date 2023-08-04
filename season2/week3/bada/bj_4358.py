'''
문제 : 생태학 (4358)
난이도 : 실버 2
주제 : 힙(heap)

#1
딕셔너리를 이용하면 되지 않을까?
나무의 이름 -> key
나무의 개수 -> value
저장할 때마다 1씩 커지는 count 변수 선언해서 전체 나무 개수 구해서 비율 출력하면 될 것 같다.
'''

import sys

tree = dict()
count = 0

while True:
    s = sys.stdin.readline().strip()
    if not s:
        break

    if s in tree:
        tree[s] += 1
    else:
        tree[s] = 1
    count += 1

# key 값을 기준으로 정렬
tree = dict(sorted(tree.items()))

for key, value in tree.items():
    print("{} {:.4f}".format(key, value/count*100))