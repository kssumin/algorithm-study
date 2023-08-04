import sys
input = sys.stdin.readline

work_bee = []
lines = sys.stdin.readlines()
for line in lines:
    work_bee = work_bee + list(line.split())

work_dict = {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}

for work in work_bee:
    if work in work_dict:
        work_dict[work] += 1


work_list = list(work_dict)
work_value = list(work_dict.values())
for i in range(7):
    print("{} {} {:.2f}".format(work_list[i], work_value[i], work_value[i]/len(work_bee)))
print("Total {} 1.00".format(len(work_bee)))
"""
풀이
벌의 일 목록들을 딕셔너리에 담아두고 value 를 0으로 초기화해준다.
벌이 한 일을 리스트에 담아두고 딕셔너리에서 확인하고 있으면 1 을 더해준다.

input = sys.stdin.readline

work_bee = []
while 1:
    try:
        work_bee.append(input().rstrip().split())
    except:
        break
        
입력받을 때 이런 식으로 했는데 왜 안되는지 모르겠다..

리스트로 추가돼서 안됐던 거였다.. 리스트에 더해줬으면 됐겠다.
ex) [[1,2,3,4],[5,6,7,8]]
"""