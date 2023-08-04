'''
1620번 - 나는야 포켓몬 마스터 이다솜
난이도 - 실버 3
알고리즘 분류 -
'''

import sys
n, m = map(int, sys.stdin.readline().split())

pokemons_num = dict()
for i in range(1, n+1):
    pokemons_num[i] = sys.stdin.readline().rstrip()
pokemons_name = {v:k for k,v in pokemons_num.items()}

for _ in range(m):
    quiz = sys.stdin.readline().rstrip()
    try:
        print(pokemons_name[quiz])
    except:
        print(pokemons_num[int(quiz)])