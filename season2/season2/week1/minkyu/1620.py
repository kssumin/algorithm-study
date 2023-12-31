import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poketmon_dict_name = dict()
poketmon_dict_num = dict()
for i in range(1, N + 1):
    poketmon = input().rstrip()
    poketmon_dict_name[poketmon] = i
    poketmon_dict_num[i] = poketmon

for i in range(M):
    quiz = input().rstrip()
    try:
        print(poketmon_dict_name[quiz])
    except:
        print(poketmon_dict_num[int(quiz)])

"""
풀이
일단 poketmon_dict_name 에 key:value 로 이름 : 숫자로 저장하고
poketmon_dict_num 에 숫자 : 이름으로 저장한다.
isdigit 함수를 쓸 생각을 못하고 type 으로 구별할 생각밖에 못해서 try except 로 풀게 되었다.
처음에 딕셔너리 name 에서 입력하게 하고 오류가 뜨면 숫자가 입력된 거니까 except 에서는 num 에서 입력하게 한다. 

처음에 type 으로 구별해서 dict 에 각각 저장해서 출력하려 했는데 (아니면 isdigit 함수)
생각해보니 input 으로 받으면 무조건 str 형이다....
또 생각해보니 포켓몬 이름에서 에러 뜨면 숫자, 숫자에서 에러 뜨면 문자니깐 그냥 try except 로 처리하면 된다! 
"""