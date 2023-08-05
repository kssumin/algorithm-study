# BJ 4358 / SILVER II / 1096ms

import sys

sys.stdin = open("input.txt", "rt")
input_trees = list(sys.stdin.readlines())
trees = []

# sys.stdin.readlines()로 입력받을 경우 줄바꿈 문자 \n이 포함됨
for tree in input_trees:
    # 그러므로 개행 문자를 제거한 원소값을 새롭게 저장한 리스트 trees를 만듦
    trees.append(tree.replace('\n', ''))

sorted_trees = sorted(trees)

trees_cnt = dict()

for tree in sorted_trees:
    if tree in trees_cnt:
        trees_cnt[tree] += 1
    else:
        trees_cnt[tree] = 1


for j in trees_cnt:
    trees_cnt[j] = (trees_cnt[j] / len(trees)) * 100

    print('{} {:.4f}'.format(j, trees_cnt[j]))


'''
NOTE:

처음에 시간 초과가 났었는데 그 이유는 딕셔너리 활용을 잘못해서였다!!

이 문제는 week1의 10816과 비슷했다.
음... 주제가 힙인 만큼 힙으로도 풀어보려고 했는데 도저히 모르겠어서 그냥 해시로 풀었다!

또 처음엔 출력문에 round()를 사용했는데 오답 처리되어서
그 이유를 찾아보았는데, round() 결과의 마지막값이 0이면 생략된다고 한다
ex) round(1.01, 1) = 1      >> 원하는 값은 1.0

이것 때문에 오답 처리된 것 같았다!
그래서 round() 말고 formatting을 사용하는 것이 좋다고 한다.

찾아보면서 부동소수점 개념도 나왔는데, 이 부분은 정리해서 추후에 이슈에 올려볼게요!

어렵당
'''