# BJ 1620 : 나는야 포켓몬 마스터 이다솜 / SILVER IV / 300ms

import sys

n, m = map(int, sys.stdin.readline().strip().split(' '))

pokemons_name = list(sys.stdin.readline().strip() for _ in range(n))
pokemons_num = list(map(str, list(i for i in range(1, n + 1))))
quest = list(sys.stdin.readline().strip() for _ in range(m))

pokemons_num_name = dict()
pokemons_name_num = dict()

for i in range(n):
    pokemons_num_name[pokemons_num[i]] = pokemons_name[i]
    pokemons_name_num[pokemons_name[i]] = pokemons_num[i]

for i in range(m):
    if quest[i] in pokemons_num_name:
        print(pokemons_num_name.get(quest[i]))
        print('')
    elif quest[i] in pokemons_name_num:
        print(pokemons_name_num.get(quest[i]))


'''
NOTE:
처음엔 key : num, value : name 인 하나의 딕셔너리를 생성했는데,
만약 quest에 name이 들어온다면 name value값으로 key값을 찾는 데에 시간이 꽤 걸리기 때문에 ( if name in list(dictionary.values()): )
아예 key : name, value : num 인 딕셔너리를 하나 더 생성했다. 

쉬운 문제 바로 맞혀서 기분이 좋다
'''