'''
9733번 - 꿀벌
난이도 - 실버 3
알고리즘 분류 -
js 포기,,
'''

# 입력
import sys
types = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']

arr = []

lines = sys.stdin.readlines()
for line in lines:
    arr = arr + list(line.split())

total = len(arr)

hashs = {}

for i in arr:
    if i in hashs:
        hashs[i] += 1
    else:
        hashs[i] = 1

for t in types:
    if t in hashs:
        print('{} {} {:.2f}'.format(t, hashs[t], hashs[t]/total))
    else:
        print('{} 0 0.00'.format(type))

print(f'Total {total} 1.00')

# 어디서 런타임 에러가 뜨는지 모르겠어요.. 찾아주세용 ㅠㅠㅜ
# 정답 코드는 민규꺼 봤습니다!